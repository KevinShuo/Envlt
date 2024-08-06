use crate::database::EnvltDataBase;
use crate::dataclass::scene_data::SceneData;
use pyo3::exceptions::PyAttributeError;
use pyo3::{pyclass, pymethods, PyResult};

#[pyclass]
#[derive(Debug)]
pub struct Projects {
    project_name: String,
    db: EnvltDataBase,
}
#[pymethods]
impl Projects {
    #[new]
    pub fn new(name: String, db_path: String) -> Self {
        let db = EnvltDataBase::new(db_path.as_str()).unwrap();
        Self {
            project_name: name,
            db,
        }
    }

    pub fn get_scenes(&self) -> PyResult<Vec<SceneData>> {
        match self.db.get_scenes(self.project_name.as_str()) {
            Some(database) => Ok(database),
            None => Err(PyAttributeError::new_err("Has not this project table")),
        }
    }

    pub fn get_scene_by_name(&self, scene_name: &str) -> Option<SceneData> {
        self.db.get_scene(self.project_name.as_str(), scene_name)
    }
}
