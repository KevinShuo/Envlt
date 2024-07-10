use chrono::Local;
use pyo3::{pyclass, pymethods};
use serde::Serialize;
use env;

#[derive(Serialize, Debug, Clone)]
#[pyclass]
pub struct SceneCSV {
    csv_path: String,
    scene_data: Vec<SceneData>,
}
#[derive(Serialize, Debug, Clone)]
#[pyclass]
pub struct SceneData {
    id: usize,
    name: String,
    image: String,
    description: String,
    create_date: String,
    modify_date: String,
    create_user: String,
    enable: bool,
}
#[pymethods]
impl SceneData {
    #[new]
    pub fn new(id: usize, name: &str, image: &str, description: &str) -> Self {
        let now_time = Local::now().format("%Y-%m-%d %H:%M:%S").to_string();
        SceneData {
            id,
            name: name.to_string(),
            image: image.to_string(),
            description: description.to_string(),
            create_date: now_time.clone(),
            modify_date: now_time,
            enable: true,
        }
    }
}
