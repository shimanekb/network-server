import server.object as obj


def test_object_repo_find_by_name_js():
    # Given
    obj_name = 'index.js'

    # When
    object = obj.ObjectRepo().find_by_name(obj_name)

    # Then
    assert object.type == obj.ContentType.APPLICATION_JAVASCRIPT
    assert 'alert(' in object.content


def test_object_repo_find_by_name_css():
    # Given
    obj_name = 'index.css'

    # When
    object = obj.ObjectRepo().find_by_name(obj_name)

    # Then
    assert object.type == obj.ContentType.TEXT_CSS
    assert 'h1 {' in object.content


def test_object_repo_find_by_name_html():
    # Given
    obj_name = 'simple.html'

    # When
    object = obj.ObjectRepo().find_by_name(obj_name)

    # Then
    assert object.type == obj.ContentType.TEXT_HTML
    assert 'Hello this is a simple html page.' in object.content


def test_object_repo_find_by_name_not_exist():
    # Given
    obj_name = 'simple_Not_real.html'

    # When
    object = obj.ObjectRepo().find_by_name(obj_name)

    # Then
    assert object is None
