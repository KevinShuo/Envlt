use chrono::Local;
use pyo3::exceptions::PyOSError;
use pyo3::prelude::*;
use std::fs::OpenOptions;
use std::io::Write;
use std::path::{Path, PathBuf};
#[pyclass]
struct EnvLog {
    full_path: PathBuf,
}
#[pymethods]
impl EnvLog {
    #[new]
    fn new(base_name: String, file_name: String) -> PyResult<Self> {
        let p = Path::new(&base_name);
        if !p.exists() {
            return Err(PyErr::new::<PyOSError, _>("Error: Base path is not exists"));
        }
        let current_date = Local::now().format("%Y-%m-%d").to_string();
        let full_file_name = format_args!("{}_{}.log", file_name, current_date).to_string();
        let full_path = p.join(full_file_name);
        if !full_path.exists() {
            OpenOptions::new()
                .write(true)
                .create_new(true)
                .open(&full_path)
                .expect("Failed to create log file");
        }
        Ok(EnvLog { full_path })
    }
    /// 写日志
    fn write_log(&self, log_level: String, content: String) -> PyResult<()> {
        let mut f_log = OpenOptions::new()
            .append(true)
            .open(&self.full_path)
            .expect("Failed to open log file");
        let local_time = Local::now().format("%H:%M:%S").to_string();
        let full_content = format_args!("{} [{log_level}] {}\n", local_time, content).to_string();
        f_log.write_all(full_content.as_bytes())?;
        Ok(())
    }
    /// 列出所有的log文件
    #[staticmethod]
    fn list_log(base_path: String, limit: Option<usize>) -> PyResult<Vec<String>> {
        let p = Path::new(&base_path);
        if !p.exists() {
            return Err(PyErr::new::<PyOSError, _>("Error: Base path is not exists"));
        }
        let mut log_list = Vec::new();
        for entry in p.read_dir()? {
            let entry = entry?;
            let file_path = entry.path();
            if file_path.to_str().unwrap().ends_with(".log") {
                log_list.push(file_path.to_str().unwrap().to_string());
            }
        }
        log_list.sort_by_key(|f| {
            f.split("_")
                .last()
                .expect("Failed to get last data")
                .to_string()
        });
        log_list.reverse();
        if let Some(l) = limit {
            log_list.truncate(l);
        }

        Ok(log_list)
    }
}
#[pymodule]
fn envlt_log(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<EnvLog>()?;
    Ok(())
}
