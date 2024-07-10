use csv::WriterBuilder;
use pyo3::{pyclass, pymethods, PyResult};
use serde::Serialize;

#[derive(Serialize, Debug, Clone)]
#[pyclass]
pub struct TextureCSV {
    csv_path: String,
    file_data: Vec<FileData>,
}

#[derive(Serialize, Debug, Default, Clone)]
#[pyclass]
pub struct FileData {
    id: usize,
    width: usize,
    height: usize,
    colorspace: String,
    node_name: String,
    file_path: String,
}
#[pymethods]
impl TextureCSV {
    #[new]
    pub fn new(csv_path: &str) -> Self {
        let tmp = csv_path.to_string();
        TextureCSV {
            csv_path: tmp,
            file_data: vec![],
        }
    }
    pub fn insert_one(&mut self, file_data: FileData) {
        self.file_data.push(file_data);
    }
    pub fn save_csv(&self) -> PyResult<()> {
        let p = &self.csv_path;
        let mut wtr = WriterBuilder::new()
            .from_path(p)
            .expect("Failed to init write builder");
        for file_datum in self.file_data.clone() {
            wtr.serialize(file_datum).expect("Failed to serialize data");
        }
        Ok(())
    }
}
#[pymethods]
impl FileData {
    #[new]
    pub fn new(
        id: usize,
        width: usize,
        height: usize,
        colorspace: &str,
        node_name: &str,
        file_path: &str,
    ) -> FileData {
        Self {
            id,
            width,
            height,
            colorspace: colorspace.to_string(),
            node_name: node_name.to_string(),
            file_path: file_path.to_string(),
        }
    }
}
