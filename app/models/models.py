from tortoise import fields, models
from tortoise.contrib.postgres.fields import ArrayField


class Municipality(models.Model):
    """Модель для хранения муниципалитетов"""

    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=128, null=False)
    down_parent_id = fields.IntField(null=True)
    tip = fields.IntField(null=False)
    id_parent = fields.IntField(null=True)
    path_id = ArrayField(null=False)
    level_parent = fields.IntField(null=False)

    class Meta:
        schema = "sp_s_subekty"
        table = "v_all_name_mo"


class AddressV2(models.Model):
    """Модель для адресов"""

    id = fields.IntField(primary_key=True)
    id_mo = fields.IntField(null=True)
    district = fields.CharField(max_length=128, null=True)
    city = fields.CharField(max_length=128, null=True)
    street = fields.CharField(max_length=128, null=True)
    house = fields.CharField(max_length=64, null=True)
    flat = fields.CharField(max_length=64, null=True)
    id_parent = fields.IntField(null=True)
    mkd = fields.BooleanField(default=False)
    is_mobile = fields.BooleanField(default=False)
    # date_create = fields.DatetimeField(auto_now_add=True)
    from_login = fields.TextField(null=True)
    deleted = fields.BooleanField(default=False)

    class Meta:
        schema = "s_gazifikacia"
        table = "t_address_v2"


class TypeValue(models.Model):
    """Модель для типов значений"""

    id = fields.IntField(primary_key=True)
    order = fields.IntField()
    type_value = fields.CharField(max_length=128, null=True)
    for_mobile = fields.BooleanField()
    description = fields.CharField(max_length=256)
    field_type_id = fields.IntField(null=True)

    class Meta:
        schema = "s_gazifikacia"
        table = "t_type_value"


class TypeAddress(models.Model):
    """Модель для типов адресов"""

    id = fields.IntField(primary_key=True)
    type_address = fields.CharField(max_length=128, null=True)

    class Meta:
        schema = "s_gazifikacia"
        table = "t_type_address"


class GazificationData(models.Model):
    """Модель для данных о газификации"""

    id = fields.IntField(primary_key=True)
    id_address = fields.IntField()
    id_type_address = fields.IntField(null=False)
    id_type_value = fields.IntField(null=True)
    value = fields.CharField(max_length=256, null=True)
    date_doc = fields.DateField(null=True)
    date = fields.DateField(null=True)
    # date_create = fields.DatetimeField(auto_now_add=True)
    is_mobile = fields.BooleanField(default=False)
    from_login = fields.TextField(null=True)
    deleted = fields.BooleanField(default=False)

    class Meta:
        schema = "s_gazifikacia"
        table = "t_gazifikacia_data"


class FieldType(models.Model):
    """Модель для типов полей"""

    field_type_id = fields.IntField(primary_key=True)
    field_type_name = fields.CharField(max_length=255, null=False)

    class Meta:
        schema = "s_gazifikacia"
        table = "field_type"


class FieldReference(models.Model):
    """Модель для связей между полями"""

    field_reference_id = fields.IntField(primary_key=True)
    field_origin_id = fields.IntField(null=False)
    field_origin_value = fields.CharField(max_length=255, null=False)
    field_ref_id = fields.IntField(null=False)

    class Meta:
        schema = "s_gazifikacia"
        table = "field_reference"


class FieldAnswer(models.Model):
    """Модель для ответов на поля"""

    field_answer_id = fields.IntField(primary_key=True)
    field_answer_value = fields.TextField(null=False)
    type_value_id = fields.IntField(null=False)
    field_size = fields.TextField(null=False)
    order = fields.IntField(default=0)

    class Meta:
        schema = "s_gazifikacia"
        table = "field_answers"


class User(models.Model):
    """Модель для пользователей системы"""

    user_id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255, null=False)
    password_hash = fields.CharField(max_length=255, null=False)

    class Meta:
        schema = "s_gazifikacia"
        table = "users"


class Activity(models.Model):
    """Модель для отслеживания активности пользователей"""

    session_id = fields.CharField(max_length=255, pk=True)
    email = fields.TextField(null=False)
    activity_count = fields.IntField(default=0)

    class Meta:
        schema = "s_gazifikacia"
        table = "activity"
