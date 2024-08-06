use pyo3::pyclass;

#[pyclass]
#[derive(Debug)]
pub struct SceneData {
    pub id: String,
    pub name: String,
    pub description: String,
    pub image: String,
    pub create_user: String,
    pub modify_user: String,
    pub create_date: String,
    pub modify_date: String,
    pub status: String,
}
