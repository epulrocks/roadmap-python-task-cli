from jsondb import TaskDB
import pytest
import os
import json

@pytest.fixture
def db_path():
    return "test_db.json"

@pytest.mark.parametrize("test_description_list", [
    (["test 1", "test 2"]),
    (["test task 2\\", "test task 3\\"]),
    ([123456, 534]),
    (["{abc}", "{abc}", "test"]),
    (["", ""])
])
def test_add(db_path, test_description_list):
    test_db = TaskDB(db_path=db_path)
    for test_description in test_description_list:
        id = test_db.add_task(test_description)
        with open(db_path, 'r') as f:
            jsondata = json.load(f)
        assert jsondata['tasks'][id]['description'] == test_description
        assert jsondata['tasks'][id]['status'] == 'todo'

@pytest.mark.parametrize("test_description_list, update_description, id", [
    (["test 1", "test 2"], "new test", 1),
    (["test task 2\\", "test task 3\\"], "new test2", 2),
    ([123456, 534], 23423, 1),
    (["{abc}", "{abc}", "test"], "", "3"),
    (["", ""], "{update", "1")
])
def test_update_description(db_path, test_description_list, update_description, id):
    test_db = TaskDB(db_path=db_path)
    updated = {}
    for test_description in test_description_list:
        new_id = test_db.add_task(test_description)
        updated[str(new_id)] = test_description
    test_db.update_task(id, 'description', update_description)
    updated[str(id)] = update_description
    for k, v in updated.items():
        with open(db_path, 'r') as f:
            jsondata = json.load(f)
        assert jsondata['tasks'][k]['description'] == v

@pytest.mark.parametrize("test_description_list, update_description, id", [
    (["test 1", "test 2"], "new test", 3),
    (["test task 2\\", "test task 3\\"], "new test2", 0),
    ([123456, 534], 23423, 3),
    (["{abc}", "{abc}", "test"], "", "4"),
    (["", ""], "{update", "3")
])
def test_update_description_invalid_id(db_path, test_description_list, update_description, id):
    test_db = TaskDB(db_path=db_path)
    for test_description in test_description_list:
        test_db.add_task(test_description)
    with pytest.raises(Exception):
        test_db.update_task(id, 'description', update_description)

@pytest.mark.parametrize("test_description_list, id", [
    (["test 1", "test 2"], 1),
    (["test task 2\\", "test task 3\\"], 2),
    ([123456, 534], 1),
    (["{abc}", "{abc}", "test"], "3"),
    (["", ""], "1")
])
def test_delete(db_path, test_description_list, id):
    test_db = TaskDB(db_path=db_path)
    updated = {}
    for test_description in test_description_list:
        new_id = test_db.add_task(test_description)
        updated[str(new_id)] = test_description
    test_db.delete_task(id)
    del updated[str(id)]
    for k, v in updated.items():
        with open(db_path, 'r') as f:
            jsondata = json.load(f)
        assert jsondata['tasks'][k]['description'] == v

@pytest.mark.parametrize("test_description_list, id", [
    (["test 1", "test 2"], 3),
    (["test task 2\\", "test task 3\\"], 0),
    ([123456, 534], 3),
    (["{abc}", "{abc}", "test"], "4"),
    (["", ""], "3")
])
def test_delete_invalid_id(db_path, test_description_list, id):
    test_db = TaskDB(db_path=db_path)
    for test_description in test_description_list:
        test_db.add_task(test_description)
    with pytest.raises(Exception):
        test_db.delete_task(id)

@pytest.fixture(autouse=True)
def cleanup(db_path):
    yield
    if os.path.exists(db_path):
        os.remove(db_path)