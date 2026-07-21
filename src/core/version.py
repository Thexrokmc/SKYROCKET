from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Version:

    major: int
    minor: int
    patch: int
    build: int = 1

    @property
    def number(self):

        return (

            f"{self.major}."

            f"{self.minor}."

            f"{self.patch}"

        )

    @property
    def full(self):

        return (

            f"{self.number}"

            f"+build.{self.build}"

        )


class VersionManager:

    VERSION = Version(

        major=1,

        minor=0,

        patch=0,

        build=1

    )

    BUILD_DATE = datetime.utcnow().isoformat()

    @classmethod
    def version(cls):

        return cls.VERSION.number

    @classmethod
    def full_version(cls):

        return cls.VERSION.full

    @classmethod
    def info(cls):

        return {

            "version": cls.version(),

            "full_version": cls.full_version(),

            "build_date": cls.BUILD_DATE

        }
