import pytest
from Exceptions import ExceptionsDemo, MyException  

def test_divide_zero():
    demo = ExceptionsDemo()
    with pytest.raises(ZeroDivisionError):
        demo.divide(10,0)

@pytest.mark.wip
def test_type_error():
    demo = ExceptionsDemo()
    with pytest.raises(TypeError):
        demo.divide('Tamaulipas',5)

@pytest.mark.wip
def test_index_error():
    demo = ExceptionsDemo()
    with pytest.raises(IndexError):
        demo.access_list([3,5,4],7)

@pytest.mark.wip
def test_index_error():
    demo = ExceptionsDemo()
    with pytest.raises((TypeError,IndexError)):
        demo.access_list([3,5,4],1)
        demo.access_list([3, 5, 4], 7)
        demo.access_list([3, 5, 4],'5')

@pytest.mark.wip
def test_key_error():
    demo = ExceptionsDemo()
    with pytest.raises(KeyError):
        demo.access_dict({'Manzana':'Dulce','Limón':'Agrio'},'Tomate')

@pytest.mark.wip
def test_FileNotFound_error():
    demo = ExceptionsDemo()
    with pytest.raises(FileNotFoundError):
        demo.read_file('frutas.txt')

@pytest.mark.wip
def test_attribute_error():
    demo = ExceptionsDemo()
    demofake = ExceptionsDemo()
    with pytest.raises(AttributeError):
        demo.access_attribute(demofake)

@pytest.mark.wip
def test_my_exception_error():
    demo = ExceptionsDemo()
    with pytest.raises(MyException):
        demo.check_positive(-3)