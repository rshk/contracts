from contracts.core.contract import Contract
from contracts.core.field import BaseField


def test_fields_schema_can_be_accessed_correctly():
    class MyContract(Contract):
        spam = BaseField()
        eggs = BaseField()
        bacon = BaseField(default='hello')

    schema = MyContract._get_fields()

    assert schema[0].name == 'spam'
    assert isinstance(schema[0].field, BaseField)

    assert schema[1].name == 'eggs'
    assert isinstance(schema[1].field, BaseField)

    assert schema[2].name == 'bacon'
    assert isinstance(schema[2].field, BaseField)
