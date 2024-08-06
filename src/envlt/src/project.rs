use crate::database::EnvltDataBase;
use crate::dataclass::scene_data::SceneData;
use pyo3::{pyclass, pymethods};

#[pyclass]
pub struct Projects {
    project_name: String,
}
#[pymethods]
impl Projects {
    #[new]
    pub fn new(name: String, envlt_db: &EnvltDataBase) -> Self {
        envlt_db.create_project(name.as_str());
        Self { project_name: name }
    }

    pub fn get_scenes(&self, envlt_db: &EnvltDataBase) -> Vec<SceneData> {
        envlt_db.get_scenes(self.project_name.as_str())
    }

    pub fn get_scene_by_name(
        &self,
        scene_name: &str,
        envlt_db: &EnvltDataBase,
    ) -> Option<SceneData> {
        envlt_db.get_scene(self.project_name.as_str(), scene_name)
    }

    pub fn delete_project(&self, envlt_db: &EnvltDataBase) {
        if let Err(err) = envlt_db.drop_table(self.project_name.as_str()) {
            eprintln!("{err:?}");
        }
    }
}
