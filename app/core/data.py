from enum import Enum

class KindOfMeteringDevices(Enum):
    """Перечисление видов приборов учёта.

    Используется для классификации типов приборов учёта потребляемых ресурсов.
    Каждое значение соответствует конкретному типу измерительного прибора.

    Attributes:
        WATER: Счетчик воды
        GAS: Счетчик газа
        HEAT: Счетчик тепла
        ELECTRICITY: Счетчик электроэнергии

    Example:
        >>> devices_kind = KindOfMeteringDevices
        >>> print(devices_kind.WATER.value)
        Счетчик воды
        >>> print(devices_kind.WATER.name)
        WATER
        >>> print(devices_kind("Счетчик воды"))
        KindOfMeteringDevices.WATER
    """
    WATER = 'Счетчик воды'
    GAS = 'Счетчик газа'
    HEAT = 'Счетчик тепла'
    ELECTRICITY = 'Счетчик электроэнергии'


class EnergySupplyExpenseTypes(Enum):
    """Перечисление видов расходов энергоснабжения.

    Определяет категории расходов на энергоресурсы в зависимости
    от целевого назначения использования энергии.

    Attributes:
        BUILDINGS_STRUCTURES: Здания и сооружения (бытовые нужды)
        PIPELINES_MAINTENANCE: Ремонт и эксплуатация газопроводов и средств ЭХЗ (технологические нужды)

    Example:
        >>> expense_types = EnergySupplyExpenseTypes
        >>> print(expense_types.BUILDINGS_STRUCTURES.value)
        Здания и сооружения
        >>> print(expense_types.BUILDINGS_STRUCTURES.name)
        BUILDINGS_STRUCTURES
        >>> print(expense_types("Здания и сооружения"))
        EnergySupplyExpenseTypes.BUILDINGS_STRUCTURES
    """
    BUILDINGS_STRUCTURES = 'Здания и сооружения'
    PIPELINES_MAINTENANCE = 'Ремонт и эксплуатация газопроводов и средств ЭХЗ'


class UtilityServiceGroups(Enum):
    """Перечисление групп видов коммунальных услуг.

    Содержит основные категории коммунальных услуг, предоставляемых
    населению и организациям для обеспечения комфортных условий жизнедеятельности.

    Attributes:
        WATER_DISPOSAL: Водоотведение (услуги по отводу сточных вод)
        WATER_SUPPLY: Водоснабжение (услуги по поставке холодной и горячей воды)
        NEGATIVE_IMPACT: Негативное воздействие на работу ЦСВ
        OTHER: Прочие коммунальные услуги
        HEAT_SUPPLY: Теплоснабжение (услуги по поставке тепловой энергии)
        ELECTRICITY_SUPPLY: Электроснабжение (услуги по поставке электрической энергии)

    Example:
        >>> service_groups = UtilityServiceGroups
        >>> print(service_groups.ELECTRICITY_SUPPLY.value)
        Электроснабжение
        >>> print(service_groups.ELECTRICITY_SUPPLY.name)
        ELECTRICITY_SUPPLY
        >>> print(service_groups("Электроснабжение"))
        UtilityServiceGroups.ELECTRICITY_SUPPLY
    """
    WATER_DISPOSAL = 'Водоотведение'
    WATER_SUPPLY = 'Водоснабжение'
    NEGATIVE_IMPACT = 'Негативное воздействие на работу ЦСВ'
    OTHER = 'Прочее'
    HEAT_SUPPLY = 'Теплоснабжение'
    ELECTRICITY_SUPPLY = 'Электроснабжение'


class EnergySupplyUnits(Enum):
    """Перечисление единиц измерения энергоснабжения.

    Определяет стандартные единицы измерения для различных видов
    энергоресурсов и коммунальных услуг.

    Attributes:
        GIGACALORIE: Гигакалория (единица измерения тепловой энергии)
        KILOWATT_HOUR: Киловатт-час (единица измерения электрической энергии)
        CUBIC_METER: Кубический метр (единица измерения объема воды и газа)
        PERCENT: Процент (относительная единица измерения)
        THOUSAND_CUBIC_METERS: Тысяча кубических метров (единица измерения больших объемов газа)
        CONVENTIONAL_UNIT: Условная единица (используется когда точное количество неизвестно)
        PIECE: Штука (единица измерения для подсчета отдельных объектов)
        HOUR: Час (единица измерения времени работы оборудования)

    Example:
        >>> units = EnergySupplyUnits
        >>> print(units.KILOWATT_HOUR.value)
        кВт*ч
        >>> print(units.KILOWATT_HOUR.name)
        KILOWATT_HOUR
        >>> print(units("кВт*ч"))
        EnergySupplyUnits.KILOWATT_HOUR
    """
    GIGACALORIE = 'Гкал'
    KILOWATT_HOUR = 'кВт*ч'
    CUBIC_METER = 'м3'
    PERCENT = '%'
    THOUSAND_CUBIC_METERS = 'тыс. м3'
    CONVENTIONAL_UNIT = 'Условная единица'
    PIECE = 'шт.'
    HOUR = 'ч.'


class CablePurposes(Enum):
    """Перечисление назначений кабелей в системах электрохимзащиты.

    Классифицирует кабели по их функциональному назначению
    в системах защиты подземных сооружений от коррозии.

    Attributes:
        POWER: Питающий кабель (для подачи электроэнергии к установкам ЭХЗ)
        DRAINAGE_AP: Дренажный кабель для компенсирующих устройств АП
        DRAINAGE_GP: Дренажный кабель для компенсирующих устройств ГП
        DRAINAGE_RAILWAY: Дренажный кабель, подключенный к рельсам железной дороги
        CONNECTION_MAIN: Соединительная магистраль (кабель для связи между установками)

    Example:
        >>> cable_purposes = CablePurposes
        >>> print(cable_purposes.POWER.value)
        Питающий
        >>> print(cable_purposes.POWER.name)
        POWER
        >>> print(cable_purposes("Питающий"))
        CablePurposes.POWER
    """
    POWER = 'Питающий'
    DRAINAGE_AP = 'Дренажный КУап'
    DRAINAGE_GP = 'Дренажный КУгп'
    DRAINAGE_RAILWAY = 'Дренажный к рельсу ЖД'
    CONNECTION_MAIN = 'Соединительная магистраль'


class ProtectedStructures(Enum):
    """Перечисление наименований защищаемых сооружений.

    Определяет типы подземных сооружений, которые защищаются
    системами электрохимической защиты от коррозии.

    Attributes:
        GAS_PIPELINE: Газопровод (магистральный или распределительный трубопровод)
        CASING: Футляр (защитный кожух для трубопроводов при пересечении препятствий)

    Example:
        >>> structures = ProtectedStructures
        >>> print(structures.GAS_PIPELINE.value)
        Газопровод
        >>> print(structures.GAS_PIPELINE.name)
        GAS_PIPELINE
        >>> print(structures("Газопровод"))
        ProtectedStructures.GAS_PIPELINE
    """
    GAS_PIPELINE = 'Газопровод'
    CASING = 'Футляр'


class MeterReadingSubmissionPeriods(Enum):
    """Перечисление периодов предоставления показаний в энергоснабжающие организации.

    Определяет сроки передачи данных приборов учёта согласно договорным обязательствам
    с энергоснабжающими компаниями.

    Attributes:
        UNTIL_20TH: Показания должны быть переданы до 20 числа текущего месяца
        UNTIL_22ND: Показания должны быть переданы до 22 числа текущего месяца
        UNTIL_23RD: Показания должны быть переданы до 23 числа текущего месяца
        UNTIL_25TH: Показания должны быть переданы до 25 числа текущего месяца
        UNTIL_MONTH_END: Показания должны быть переданы до окончания текущего месяца
        HALF_YEAR: Показания предоставляются с периодичностью раз в полгода

    Example:
        >>> periods = MeterReadingSubmissionPeriods
        >>> print(periods.UNTIL_25TH.value)
        До 25 числа отчетного месяца
        >>> print(periods.UNTIL_25TH.name)
        UNTIL_25TH
        >>> print(periods("До 25 числа отчетного месяца"))
        MeterReadingSubmissionPeriods.UNTIL_25TH
    """
    UNTIL_20TH = 'До 20 числа отчетного месяца'
    UNTIL_22ND = 'До 22 числа отчетного месяца'
    UNTIL_23RD = 'До 23 числа отчетного месяца'
    UNTIL_25TH = 'До 25 числа отчетного месяца'
    UNTIL_MONTH_END = 'До конца месяца'
    HALF_YEAR = 'Полугодие'


class AnodeGroundingPlacements(Enum):
    """Перечисление расположений анодных заземлений.

    Определяет пространственную ориентацию анодных заземлений
    в системах электрохимической защиты.

    Attributes:
        HORIZONTAL: Горизонтальное расположение (заземлитель уложен в траншее)
        VERTICAL: Вертикальное расположение (заземлитель установлен вертикально в грунте)

    Example:
        >>> placements = AnodeGroundingPlacements
        >>> print(placements.VERTICAL.value)
        Вертикально
        >>> print(placements.VERTICAL.name)
        VERTICAL
        >>> print(placements("Вертикально"))
        AnodeGroundingPlacements.VERTICAL
    """
    HORIZONTAL = 'Горизонтально'
    VERTICAL = 'Вертикально'


class PrimaryDocumentsReceivingMethods(Enum):
    """Перечисление способов получения первичных документов энергоснабжения.

    Описывает различные каналы получения расчетных документов
    от энергоснабжающих организаций.

    Attributes:
        IN_PERSON: Личное получение (документы забираются курьером или представителем)
        MAIL: Почтовые отправления (документы приходят традиционной почтой)
        EMAIL: Электронная почта (документы отправляются на email в электронном виде)
        OTHER: Прочие способы получения документов
        EDI: Электронный документооборот (через специализированные системы ЭДО)

    Example:
        >>> methods = PrimaryDocumentsReceivingMethods
        >>> print(methods.EDI.value)
        ЭДО
        >>> print(methods.EDI.name)
        EDI
        >>> print(methods("ЭДО"))
        PrimaryDocumentsReceivingMethods.EDI
    """
    IN_PERSON = 'Нарочно'
    MAIL = 'По почте'
    EMAIL = 'По электронной почте'
    OTHER = 'Прочее'
    EDI = 'ЭДО'


class RouteTerritorialAffiliations(Enum):
    """Перечисление территориальных принадлежностей маршрутов.

    Классифицирует маршруты обслуживания по их территориальной
    принадлежности к различным зонам обслуживания.

    Attributes:
        URBAN: Городской маршрут (обслуживание объектов в городской черте)
        ZARECHNY: Заречный маршрут (обслуживание объектов в Заречной зоне)

    Example:
        >>> routes = RouteTerritorialAffiliations
        >>> print(routes.URBAN.value)
        Городской
        >>> print(routes.URBAN.name)
        URBAN
        >>> print(routes("Городской"))
        RouteTerritorialAffiliations.URBAN
    """
    URBAN = 'Городской'
    ZARECHNY = 'Заречный'


class ECPTerritorialAffiliations(Enum):
    """Перечисление территориальных принадлежностей ЭХЗ.

    Определяет территориальную классификацию объектов
    электрохимической защиты по типу населенного пункта.

    Attributes:
        CITY: Городская территория (объекты ЭХЗ расположены в городе)
        VILLAGE: Сельская территория (объекты ЭХЗ расположены в селе)

    Example:
        >>> territories = ECPTerritorialAffiliations
        >>> print(territories.CITY.value)
        Город
        >>> print(territories.CITY.name)
        CITY
        >>> print(territories("Город"))
        ECPTerritorialAffiliations.CITY
    """
    CITY = 'Город'
    VILLAGE = 'Село'


class AnodeGroundingTypes(Enum):
    """Перечисление типов анодных заземлений.

    Классифицирует анодные заземления по их конструктивному
    исполнению и способу установки в грунт.

    Attributes:
        DEEP: Глубинное заземление (устанавливается на значительную глубину)
        SURFACE: Поверхностное заземление (устанавливается в верхних слоях грунта)

    Example:
        >>> grounding_types = AnodeGroundingTypes
        >>> print(grounding_types.DEEP.value)
        Глубинное
        >>> print(grounding_types.DEEP.name)
        DEEP
        >>> print(grounding_types("Глубинное"))
        AnodeGroundingTypes.DEEP
    """
    DEEP = 'Глубинное'
    SURFACE = 'Поверхностное'


class RoadCrossingTypes(Enum):
    """Перечисление типов переходов под дорогами.

    Определяет категории автомобильных и железнодорожных путей,
    под которыми прокладываются защищаемые сооружения.

    Attributes:
        AUTOMOBILE: Автомобильная дорога (переход под автодорогой любого класса)
        RAILWAY: Железная дорога (переход под железнодорожными путями)

    Example:
        >>> crossings = RoadCrossingTypes
        >>> print(crossings.RAILWAY.value)
        Железнодорожный
        >>> print(crossings.RAILWAY.name)
        RAILWAY
        >>> print(crossings("Железнодорожный"))
        RoadCrossingTypes.RAILWAY
    """
    AUTOMOBILE = 'Автомобильный'
    RAILWAY = 'Железнодорожный'


class ECPSupplyLineTypes(Enum):
    """Перечисление типов питающих линий установок ЭХЗ.

    Классифицирует линии электропередачи, используемые для
    питания установок электрохимической защиты.

    Attributes:
        OVERHEAD_LINE: Воздушная линия (ЛЭП, смонтированная на опорах над землей)
        CABLE_LINE: Кабельная линия (ЛЭП, проложенная кабелем в земле или по конструкциям)

    Example:
        >>> line_types = ECPSupplyLineTypes
        >>> print(line_types.OVERHEAD_LINE.value)
        ВЛ
        >>> print(line_types.OVERHEAD_LINE.name)
        OVERHEAD_LINE
        >>> print(line_types("ВЛ"))
        ECPSupplyLineTypes.OVERHEAD_LINE
    """
    OVERHEAD_LINE = 'ВЛ'
    CABLE_LINE = 'КЛ'


class CPSConverterTypes(Enum):
    """Перечисление типов преобразователей станций катодной защиты.

    Определяет технологические типы преобразователей, используемых
    в станциях катодной защиты для преобразования электрической энергии.

    Attributes:
        TRANSFORMER: Трансформаторный преобразователь (на основе силового трансформатора)
        INVERTER: Инверторный преобразователь (на основе полупроводниковых элементов)

    Example:
        >>> converter_types = CPSConverterTypes
        >>> print(converter_types.INVERTER.value)
        Инверторный
        >>> print(converter_types.INVERTER.name)
        INVERTER
        >>> print(converter_types("Инверторный"))
        CPSConverterTypes.INVERTER
    """
    TRANSFORMER = 'Трансформаторный'
    INVERTER = 'Инверторный'


class ECPInstallationTypes(Enum):
    """Перечисление типов установок электрохимической защиты.

    Содержит основные типы установок ЭХЗ, различающиеся по
    принципу действия и способу защиты от коррозии.

    Attributes:
        CATHODIC: Катодная установка (защита путем катодной поляризации сооружения)
        DRAINAGE: Дренажная установка (защита путем отвода блуждающих токов)
        PROTECTOR: Протекторная установка (защита с помощью протекторов)
        ISOLATING_JOINTS: Изолирующие соединения (устройства для электрической изоляции)

    Example:
        >>> installation_types = ECPInstallationTypes
        >>> print(installation_types.CATHODIC.value)
        Катодная
        >>> print(installation_types.CATHODIC.name)
        CATHODIC
        >>> print(installation_types("Катодная"))
        ECPInstallationTypes.CATHODIC
    """
    CATHODIC = 'Катодная'
    DRAINAGE = 'Дренажная'
    PROTECTOR = 'Протекторная'
    ISOLATING_JOINTS = 'Изолирующие соединения'