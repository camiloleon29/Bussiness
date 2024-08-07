import pydantic


class Holiday(pydantic.BaseModel):
    description: str
    month: int
    day: int


class ColombianHoliday(Holiday):
    move_to_monday: bool


COLOMBIAN_HOLIDAYS = [
    ColombianHoliday(
        move_to_monday=False,
        description="Año Nuevo",
        month=1,
        day=1
    ),
    ColombianHoliday(
        move_to_monday=False,
        description="Reyes Magos",
        month=1,
        day=1
    ),
    ColombianHoliday(
        move_to_monday=False,
        description="Día de San José",
        month=1,
        day=1
    ),
    ColombianHoliday(
        move_to_monday=False,
        description="Dia del trabajo",
        month=1,
        day=1
    ),
    ColombianHoliday(
        move_to_monday=False,
        description="Ascensión de Jesús",
        month=1,
        day=1
    ),
    ColombianHoliday(
        move_to_monday=False,
        description="Corpus Christi",
        month=1,
        day=1
    ),
    ColombianHoliday(
        move_to_monday=False,
        description="Sagrado Corazón de Jesús",
        month=1,
        day=1
    ),
    ColombianHoliday(
        move_to_monday=False,
        description="San Pedro y San Pablo",
        month=1,
        day=1
    ),
    ColombianHoliday(
        move_to_monday=False,
        description="Día de la independencia",
        month=1,
        day=1
    ),
    ColombianHoliday(
        move_to_monday=False,
        description="Batalla de Boyacá",
        month=1,
        day=1
    ),
    ColombianHoliday(
        move_to_monday=False,
        description="Asunción de la Virgen",
        month=1,
        day=1
    ),
    ColombianHoliday(
        move_to_monday=False,
        description="Día de la raza",
        month=1,
        day=1
    ),
    ColombianHoliday(
        move_to_monday=False,
        description="Todos los Santos",
        month=1,
        day=1
    ),
    ColombianHoliday(
        move_to_monday=False,
        description="Independencia de Cartagena",
        month=1,
        day=1
    ),
    ColombianHoliday(
        move_to_monday=False,
        description="Inmaculada Concepcióna",
        month=1,
        day=1
    ),
    ColombianHoliday(
        move_to_monday=False,
        description="Navidad",
        month=1,
        day=1
    ),
]