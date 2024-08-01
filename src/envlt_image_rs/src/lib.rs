use std::path::Path;
use image::GenericImageView;
use image::imageops::FilterType;
use image::io::Reader;
use pyo3::prelude::*;
use pyo3::exceptions::{PyOSError};

#[pyclass]
struct Image {
    image_path: String,
    save_path: String,
}
#[pyclass]
struct ImageSize {
    width: u32,
    height: u32,
}
#[pymethods]
impl Image {
    #[new]
    fn new(image_path: String, save_path: String) -> PyResult<Self> {
        let p_image = Path::new(&image_path);
        if !p_image.exists() {
            return Err(PyErr::new::<PyOSError, _>("Error: Image is not exists"));
        }
        Ok(
            Image {
                image_path,
                save_path,
            }
        )
    }

    fn resize_image(&self, width: u32, height: u32) {
        let image = Reader::open(&self.image_path).expect("Failed to open").decode().expect("Failed to decode");
        let new_image = image.resize(width, height, FilterType::Nearest);
        new_image.save(&self.save_path).expect("Failed to save image");
    }

    fn get_image_size(&self) -> PyResult<ImageSize> {
        let image = Reader::open(&self.image_path).expect("Failed to open image").decode().expect("Failed to decode image");
        let size = ImageSize {
            width: image.width(),
            height: image.height(),
        };
        Ok(size)
    }
}

#[pymethods]
impl ImageSize {
    #[getter]
    fn width(&self) -> PyResult<u32> {
        Ok(self.width)
    }

    #[getter]
    fn height(&self) -> PyResult<u32> {
        Ok(self.height)
    }
}

#[pyclass]
struct Image2 {
    image_path: String,
    save_path: String,
}
#[pymethods]
impl Image2 {}

#[pymodule]
#[pyo3(name = "envlt_image")]
fn envlt_image_rs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<Image>()?;
    Ok(())
}