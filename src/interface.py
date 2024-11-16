from abc import ABC, abstractmethod


class DiagnosticDevice(ABC):
    """Прибор диагностики

    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
    def inspection(self) -> str:
        """Осмотр

        Raises:
            NotImplementedError: _description_

        Returns:
            str: _description_
        """
        raise NotImplementedError()


class SurgicalInstrument(ABC):
    """Прибор хирургический

    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
    def inspection(self) -> str:
        """Осмотр

        Raises:
            NotImplementedError: _description_

        Returns:
            str: _description_
        """
        raise NotImplementedError()


class RehabilitationDevice(ABC):
    """Прибор реабилитации

    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
    def inspection(self) -> str:
        """Осмотр

        Raises:
            NotImplementedError: _description_

        Returns:
            str: _description_
        """
        raise NotImplementedError()


class MedicalEquipmentFactory(ABC):
    """Медицинская фабрика

    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
    def create_device(self):
        raise NotImplementedError()
    
    @abstractmethod
    def create_second_device(self):
        raise NotImplementedError()