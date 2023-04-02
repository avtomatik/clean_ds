# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 21:43:02 2020

@author: Alexander Mikhailov
"""

import os
import shutil
import zipfile
from pathlib import Path
from zipfile import ZipFile


def zip_del_pack(archive_name: str, file_names: tuple[str], deletion: tuple[str]) -> None:
    with ZipFile(f'{archive_name}.zip', 'w') as archive:
        for file_name in file_names:
            archive.write(file_name, compress_type=zipfile.ZIP_DEFLATED)
    for file_name in deletion:
        os.unlink(file_name)


DIR = 'C:\\Projects\\__migration__'
FILE_NAMES = (
    'reference-en-douglas-p-h-cobb-douglas_production_function_once_again_en.tex',
    'reference-en-douglas-p-h-cobb-douglas_production_function_once_again_ru.tex',
    'reference-en-samuelson-p-a-paul_douglas_s_measurement.tex',
    'reference-en-douglas-p-h-cobb-douglas_production_function_once_again_en.pdf',
    'reference-en-douglas-p-h-cobb-douglas_production_function_once_again_ru.pdf',
    'reference-en-samuelson-p-a-paul_douglas_s_measurement.pdf',
)
MATCHERS = ('_reference', )

kwargs = {
    'archive_name': 'projectCensusComplex',
    'file_names': (
        'projectCensusComplex.py',
        'projectCensusComplexPlotKZF.pdf',
        'projectCensusComplexPlotKZF.xlsm',
        'projectCensusComplexPlotPearsonRTest.xlsm',
        'projectCensusComplexPlotSES.xlsm',
        'dataset_uscb.zip',
        'dataset_uscb.zip',
        'dataset_usa_cobb-douglas.zip',
        'dataset_douglas.zip',
    ),
    'deletion': (
        'projectCensusComplex.py',
        'projectCensusComplexPlotKZF.pdf',
        'projectCensusComplexPlotKZF.xlsm',
        'projectCensusComplexPlotPearsonRTest.xlsm',
        'projectCensusComplexPlotSES.xlsm',
    ),
}

kwargs = {
    'archive_name': 'projectApproximation',
    'file_names': (
        'projectApproximation.py',
        'projectApproximationPlotApproxLinear.xlsm',
        'projectApproximationPlotApproxLogLinearA.xlsm',
        'projectApproximationPlotApproxLogLinearB.xlsm',
        'dataset_uscb.zip',
        'dataset_usa_0022_m1.txt',
        'dataset_usa_0025_p_r.txt',
        'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1929_1969.zip',
        'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1969_2012.zip',
        'dataset_usa_bea-sfat-release-2012-08-15-SectionAll_xls.zip',
        'dataset USA FRB_H6.csv',
        'mcConnellBrue.zip',
    ),
    'deletion': (
        'projectApproximation.py',
        'projectApproximationPlotApproxLinear.xlsm',
        'projectApproximationPlotApproxLogLinearA.xlsm',
        'projectApproximationPlotApproxLogLinearB.xlsm',
    ),
}

kwargs = {
    'archive_name': 'projectCapital',
    'file_names': (
        'projectCapital.py',
        'projectCapitalInteractive.py',
        'projectCapital.pdf',
        'projectCapitalInteractiveCapitalAcquisitions.xlsm',
        'projectCapitalInteractiveCapitalRetirement.xlsm',
        'NipaDataA.txt',
        'dataset USA BLS cpiai.txt',
        'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1929_1969.zip',
        'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1969_2012.zip',
        'dataset USA FRB_G17_All_Annual 2013-06-23.csv',
        'dataset_usa_bea-sfat-release-2017-08-23-SectionAll_xls.zip',
    ),
    'deletion': (
        'projectCapital.py',
        'projectCapitalInteractive.py',
        'projectCapital.pdf',
        'projectCapitalInteractiveCapitalAcquisitions.xlsm',
        'projectCapitalInteractiveCapitalRetirement.xlsm',
    ),
}

kwargs = {
    'archive_name': 'projectElasticity',
    'file_names': (
        'projectElasticity.py',
        'projectElasticityPlotElasticity.docx',
        'projectElasticityPlotElasticity.xlsm',
        'dataset_uscb.zip',
        'dataset_usa_0022_m1.txt',
        'dataset_usa_0025_p_r.txt',
        'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1929_1969.zip',
        'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1969_2012.zip',
        'dataset_usa_bea-sfat-release-2012-08-15-SectionAll_xls.zip',
        'dataset USA FRB_H6.csv',
    ),
    'deletion': (
        'projectElasticity.py',
        'projectElasticityPlotElasticity.docx',
        'projectElasticityPlotElasticity.xlsm',
    ),
}

kwargs = {
    'archive_name': 'projectMSpline',
    'file_names': (
        'projectMSpline.py',
        'projectMSplineEA.xlsm',
        'projectMSplineEB.xlsm',
        'projectMSplineLA.xlsm',
        'projectMSplineLB.xlsm',
        'projectMSplineLLS.xlsm',
        'projectMSplineE.docx',
        'projectMSplineL.docx',
        'projectMSplineLLS.docx',
        'dataset_uscb.zip',
        'dataset_usa_cobb-douglas.zip',
        'dataset_douglas.zip',
    ),
    'deletion': (
        'projectMSpline.py',
        'projectMSplineEA.xlsm',
        'projectMSplineEB.xlsm',
        'projectMSplineLA.xlsm',
        'projectMSplineLB.xlsm',
        'projectMSplineLLS.xlsm',
        'projectMSplineE.docx',
        'projectMSplineL.docx',
        'projectMSplineLLS.docx',
    ),
}

kwargs = {
    'archive_name': 'projectAntipov',
    'file_names': (
        'projectAntipov.py',
        'projectAntipov.docx',
        'projectAntipov.pdf',
        'dataset_uscb.zip',
        'dataset_usa_0022_m1.txt',
        'dataset_usa_0025_p_r.txt',
        'NipaDataA.txt',
        'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1929_1969.zip',
        'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1969_2012.zip',
        'dataset_usa_bea-release-2015-02-27-SectionAll_xls_1929_1969.zip',
        'dataset_usa_bea-release-2015-02-27-SectionAll_xls_1969_2015.zip',
        'dataset_usa_bea-sfat-release-2012-08-15-SectionAll_xls.zip',
        'dataset_usa_bea-sfat-release-2017-08-23-SectionAll_xls.zip',
        'dataset USA FRB_H6.csv',
    ),
    'deletion': (
        'projectAntipov.py',
        'projectAntipov.docx',
        'projectAntipov.pdf',
    ),
}

kwargs = {
    'archive_name': 'projectPrices',
    'file_names': (
        'prices.py',
        'prices.pdf',
        'pricesDatasetBeaGdp.xlsm',
        'pricesDirect.xlsm',
        'pricesInverse.xlsm',
        'dataset USA BEA GDPDEF.xls',
        'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1929_1969.zip',
        'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1969_2012.zip',
        'dataset USA BLS cpiai.txt',
    ),
    'deletion': (
        'prices.py',
        'prices.pdf',
        'pricesDatasetBeaGdp.xlsm',
        'pricesDirect.xlsm',
        'pricesInverse.xlsm',
    ),
}

kwargs = {
    'archive_name': 'projectAutocorrelation',
    'file_names': (
        'projectAutocorrelation.py',
        'projectAutocorrelation.xlsm',
        'projectAutocorrelationAlpha.docx',
        'projectAutocorrelationAlpha.pdf',
        'CHN_TUR_GDP.zip',
        'dataset USA FRB_G17_All_Annual 2013-06-23.csv',
        'datasetAutocorrelation.txt',
    ),
    'deletion': (
        'projectAutocorrelation.py',
        'projectAutocorrelation.xlsm',
        'projectAutocorrelationAlpha.docx',
        'projectAutocorrelationAlpha.pdf',
        'CHN_TUR_GDP.zip',
        'datasetAutocorrelation.txt',
    ),
}

kwargs = {
    'archive_name': 'graduate_project',
    'file_names': (
        'Graduate Project fg_s.xlsx',
        'Graduate Project Financial Plan Revised.xlsx',
        'Graduate Project Financial Plan.xlsx',
        'Graduate Project Method Pyati Sil Portera.xlsx',
        'Graduate Project Sales Forecast.xlsx',
        'Graduate Project.xlsx',
        'Graduate Project-1.xlsx',
    ),
}
{
    'file_names': (
        'favppvpdf.pdf',
        'GraphDd1-12.zip',
        'TableDd1-12-csv.zip',
        'TableDd1-12-ris.zip',
        'TablePdf.jsp',
    )
}

matching = [
    file_name for file_name in os.listdir() if all(pattern in file_name for pattern in MATCHERS)
]
fn_in = "reference_en_douglas1976.pdf"
fn_ot = "reference-en-douglas-p-h-cobb-douglas_production_function_once_again.pdf"
# =============================================================================
# shutil.copy2(
#     Path("C:").joinpath(fn_in),
#     Path("D:").joinpath(fn_in)
# )
# =============================================================================

# =============================================================================
# for file_name in FILE_NAMES:
#     shutil.copy2(
#         Path('C:\\Projects\\Latex').joinpath(file_name),
#         Path('D:').joinpath(file_name)
#     )
#
#
# push_files_to_zip('vba_scripts', tuple(os.listdir()))
# zip_del_pack(**kwargs)
# push_files_to_zip(**kwargs)
# =============================================================================

# =============================================================================
# file_names = tuple(file_name for file_name in os.listdir()
#                    if file_name != 'scripts.zip')
# for file_name in tuple(os.listdir()):
#     if file_name.startswith(('rozhdestvo_ooo', )):
#         pass
# =============================================================================
