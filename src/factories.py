from typing import Union

from src.teacher_query_tools import ANLITeacherQuerier, CQATeacherQuerier, ESNLITeacherQuerier, SVAMPTeacherQuerier
from src.teacher_response_parser import (
    ANLITeacherResponseParser,
    CQATeacherResponseParser,
    ESNLITeacherResponseParser,
    SVAMPTeacherResponseParser,
)

import importlib

dsbs_data_utils = importlib.import_module("distilling-step-by-step.data_utils")


def dataLoaderFactory(
    dataset_name: str,
) -> Union[
    dsbs_data_utils.ANLI1DatasetLoader,
    dsbs_data_utils.CQADatasetLoader,
    dsbs_data_utils.ESNLIDatasetLoader,
    dsbs_data_utils.SVAMPDatasetLoader,
]:
    if dataset_name == "anli1":
        return dsbs_data_utils.ANLI1DatasetLoader()
    elif dataset_name == "cqa":
        return dsbs_data_utils.CQADatasetLoader()
    elif dataset_name == "esnli":
        return dsbs_data_utils.ESNLIDatasetLoader()
    elif dataset_name == "svamp":
        return dsbs_data_utils.SVAMPDatasetLoader()


def teacherQuerierFactory(
    dataset_name: str,
) -> Union[ANLITeacherQuerier, CQATeacherQuerier, ESNLITeacherQuerier, SVAMPTeacherQuerier]:
    if dataset_name == "anli1":
        return ANLITeacherQuerier()
    elif dataset_name == "cqa":
        return CQATeacherQuerier()
    elif dataset_name == "esnli":
        return ESNLITeacherQuerier()
    elif dataset_name == "svamp":
        return SVAMPTeacherQuerier()


def teacherResponseParserFactory(
    dataset_name: str,
) -> Union[ANLITeacherResponseParser, CQATeacherResponseParser, ESNLITeacherResponseParser, SVAMPTeacherResponseParser]:
    if dataset_name == "anli1":
        return ANLITeacherResponseParser()
    elif dataset_name == "cqa":
        return CQATeacherResponseParser()
    elif dataset_name == "esnli":
        return ESNLITeacherResponseParser()
    elif dataset_name == "svamp":
        return SVAMPTeacherResponseParser()
