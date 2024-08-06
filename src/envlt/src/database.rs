use crate::dataclass::scene_data::SceneData;
use pyo3::exceptions::PyAttributeError;
use pyo3::{pyclass, pymethods, PyResult};
use sqlite::{Connection, State, Statement};

#[pyclass]
pub struct EnvltDataBase {
    connection: Connection,
}
#[pymethods]
impl EnvltDataBase {
    #[new]
    pub fn new(path: &str) -> PyResult<Self> {
        let connect = sqlite::open(path).expect("Can't find sqlite file");
        Ok(Self {
            connection: connect,
        })
        // Self { path }
    }

    pub fn create_project(&self, name: &str) {
        if !self.check_table_exists(name) {
            let argv = format!(
                "create table {}
(
    id          integer not null
        constraint project_name_pk
            primary key autoincrement
        constraint project_name_pk_2
            unique,
    name        TEXT    not null,
    description TEXT,
    image       TEXT,
    create_user TEXT,
    modify_user TEXT,
    create_date TEXT,
    modify_date TEXT,
    status      TEXT
);",
                name
            );
            self.connection.execute(argv).unwrap();
        } else {
            eprintln!("[WARNING] Table: {name} is exists");
        }
    }

    pub fn get_all_projects(&self) -> Vec<String> {
        let query = "SELECT *
FROM sqlite_master
WHERE type = 'table'
  and name != 'sqlite_sequence'";
        let mut statement = self.connection.prepare(query).unwrap();
        let mut tables = vec![];
        while let Ok(State::Row) = statement.next() {
            let name = statement.read::<String, _>("name").unwrap();
            tables.push(name);
        }
        tables
    }

    pub fn get_scenes(&self, project_name: &str) -> Vec<SceneData> {
        let mut v = vec![];
        let query = format!(r"SELECT * FROM {}", project_name);
        let mut statement = self.connection.prepare(query).expect("Has not this table");
        while let Ok(State::Row) = statement.next() {
            v.push(get_scene_data(&mut statement))
        }
        v
    }

    pub fn get_scene(&self, project_name: &str, scene_name: &str) -> Option<SceneData> {
        let query = format!(
            "SELECT * FROM {} where name = '{}'",
            project_name, scene_name
        );
        let mut statement = self.connection.prepare(query).unwrap();
        while let Ok(State::Row) = statement.next() {
            return Some(get_scene_data(&mut statement));
        }
        return None;
    }

    pub fn drop_table(&self, table: &str) -> PyResult<()> {
        let query = format!("drop table {};", table);
        Ok(self.connection.execute(query).unwrap())
    }

    fn check_table_exists(&self, table_name: &str) -> bool {
        let query = format!(
            "SELECT * FROM sqlite_master where type = 'table' and name = '{}'",
            table_name
        );
        let mut statement = self.connection.prepare(query).unwrap();
        statement.iter().next().is_some()
    }
}
fn get_scene_data(statement: &mut Statement) -> SceneData {
    let id = statement.read::<String, _>("id").unwrap();
    let name = statement.read::<String, _>("name").unwrap();
    let description = statement.read::<String, _>("description").unwrap();
    let image = statement.read::<String, _>("image").unwrap();
    let create_user = statement.read::<String, _>("create_user").unwrap();
    let modify_user = statement.read::<String, _>("modify_user").unwrap();
    let create_date = statement.read::<String, _>("create_date").unwrap();
    let modify_date = statement.read::<String, _>("modify_date").unwrap();
    let status = statement.read::<String, _>("status").unwrap();
    SceneData {
        id,
        name,
        description,
        image,
        create_user,
        modify_user,
        create_date,
        modify_date,
        status,
    }
}

#[cfg(test)]
mod tests {
    use crate::database::EnvltDataBase;

    #[test]
    fn test_create_table() {
        let p = r"C:\dev\maya\Envlt\src\database\envlt_db.sqlite";
        let e = EnvltDataBase::new(p).unwrap();
        e.create_project("project_1_test");
        println!("{:#?}", e.get_scenes("project_1_test"));
    }
    #[test]
    fn test_check_table_exists() {
        let p = r"C:\dev\maya\Envlt\src\database\envlt_db.sqlite";
        let e = EnvltDataBase::new(p).unwrap();
        e.check_table_exists("project_name");
    }
}
