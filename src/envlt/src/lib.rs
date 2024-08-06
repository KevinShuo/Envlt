mod database;
mod dataclass;
mod project;

use crate::database::EnvltDataBase;
use crate::project::Projects;
use pyo3::exceptions::PyAttributeError;
use pyo3::prelude::*;

#[pyclass]
struct EnvltRs {
    db: EnvltDataBase,
    path: String,
}
#[pymethods]
impl EnvltRs {
    #[new]
    pub fn new(db: &str) -> Self {
        let env_db = EnvltDataBase::new(db).unwrap();
        Self {
            db: env_db,
            path: db.to_string(),
        }
    }

    pub fn new_project(&self, name: &str) -> Projects {
        self.db.create_project(name);
        Projects::new(name.to_string(), self.path.clone())
    }

    pub fn get_all_projects(&self) -> Vec<Projects> {
        let mut v = vec![];
        let project_data = self.db.get_all_projects();
        for data in project_data {
            v.push(Projects::new(data, self.path.clone()));
        }
        v
    }

    pub fn get_project_by_name(&self, project_name: &str) -> PyResult<Projects> {
        if !self.db.check_table_exists(project_name) {
            Err(PyAttributeError::new_err("This project is not exists"))
        } else {
            Ok(Projects::new(project_name.to_string(), self.path.clone()))
        }
    }

    pub fn delete_project(&self, project_name: &str) -> PyResult<()> {
        self.db.drop_table(project_name)
    }
}

#[cfg(test)]
mod tests {
    use crate::EnvltRs;

    #[test]
    fn test_new_project() {
        let e = EnvltRs::new(r"I:\DEV\Python\Envlt\database\envlt_db.sqlite");
        e.new_project("my_project_1");
        println!("{:#?}", e.get_all_projects());
    }

    #[test]
    fn check_get_project_by_name() {
        let e = EnvltRs::new(r"I:\DEV\Python\Envlt\database\envlt_db.sqlite");
        println!("{:?}", e.get_project_by_name("aa"));
    }
}
