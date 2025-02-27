import data
from data import CountyDemographics
from typing import List

# Part 1
def population_total(data: list[CountyDemographics]) -> int:
    return sum(county.population['2014 Population'] for county in data)

# Part 2
def filter_by_state(dataset: List[data.CountyDemographics], state: str) -> List[data.CountyDemographics]:
    return [county for county in dataset if county.state == state]

# Part 3
def population_by_education(dataset: List[data.CountyDemographics], education_level: str) -> int:
    return sum((county.education[education_level] / 100) * county.population['2014 Population'] for county in dataset if
               education_level in county.education)


def population_by_ethnicity(dataset: List[data.CountyDemographics], ethnicity: str) -> int:
    return sum((county.ethnicities[ethnicity] / 100) * county.population['2014 Population'] for county in dataset if
               ethnicity in county.ethnicities)


def population_below_poverty_level(dataset: List[data.CountyDemographics]) -> int:
    return sum((county.income['Persons Below Poverty Level'] / 100) * county.population['2014 Population'] for county in
               dataset if 'Persons Below Poverty Level' in county.income)

# Part 4
def percent_by_education(dataset: List[data.CountyDemographics], education_level: str) -> float:
    total_population = population_total(dataset)
    if total_population == 0:
        return 0.0
    return (population_by_education(dataset, education_level) / total_population) * 100


def percent_by_ethnicity(dataset: List[data.CountyDemographics], ethnicity: str) -> float:
    total_population = population_total(dataset)
    if total_population == 0:
        return 0.0
    return (population_by_ethnicity(dataset, ethnicity) / total_population) * 100


def percent_below_poverty_level(dataset: List[data.CountyDemographics]) -> float:
    total_population = population_total(dataset)
    if total_population == 0:
        return 0.0
    return (population_below_poverty_level(dataset) / total_population) * 100

# Part 5
def education_greater_than(dataset: List[data.CountyDemographics], education_level: str, threshold: float) -> List[data.CountyDemographics]:
    return [county for county in dataset if county.education.get(education_level, 0) > threshold]

def education_less_than(dataset: List[data.CountyDemographics], education_level: str, threshold: float) -> List[data.CountyDemographics]:
    return [county for county in dataset if county.education.get(education_level, 0) < threshold]

def ethnicity_greater_than(dataset: List[data.CountyDemographics], ethnicity: str, threshold: float) -> List[data.CountyDemographics]:
    return [county for county in dataset if county.ethnicities.get(ethnicity, 0) > threshold]

def ethnicity_less_than(dataset: List[data.CountyDemographics], ethnicity: str, threshold: float) -> List[data.CountyDemographics]:
    return [county for county in dataset if county.ethnicities.get(ethnicity, 0) < threshold]

def below_poverty_level_greater_than(dataset: List[data.CountyDemographics], threshold: float) -> List[data.CountyDemographics]:
    return [county for county in dataset if county.income.get('Persons Below Poverty Level', 0) > threshold]

def below_poverty_level_less_than(dataset: List[data.CountyDemographics], threshold: float) -> List[data.CountyDemographics]:
    return [county for county in dataset if county.income.get('Persons Below Poverty Level', 0) < threshold]
