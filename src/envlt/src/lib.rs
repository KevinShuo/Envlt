mod database;
mod dataclass;
mod project;

use crate::database::EnvltDataBase;
use crate::project::Projects;
use pyo3::prelude::*;

#[pyclass]
struct Envlt_rs {
    db: EnvltDataBase,
}
#[pymethods]
impl Envlt_rs {
    #[new]
    pub fn new(db: &str) -> Self {
        let env_db = EnvltDataBase::new(db).unwrap();
        Self { db: env_db }
    }

    pub fn new_project(&self, name: &str) {
        Projects::new(name.to_string(), &self.db);
    }

    pub fn get_all_projects(&self) -> Vec<String> {
        self.db.get_all_projects()
    }
}

#[cfg(test)]
mod tests {
    use crate::Envlt_rs;

    #[test]
    fn test_new_project() {
        let e = Envlt_rs::new(r"C:\dev\maya\Envlt\src\database\envlt_db.sqlite");
        e.new_project("my_project_1");
        println!("{:#?}",e.get_all_projects());
    }
}
