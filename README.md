[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.2+-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![NumPy](https://img.shields.io/badge/NumPy-1.26+-013243?logo=numpy&logoColor=white)](https://numpy.org)
[![SciPy](https://img.shields.io/badge/SciPy-1.13+-8CAAE6?logo=scipy&logoColor=white)](https://scipy.org)
[![Plotly](https://img.shields.io/badge/Plotly-5.24+-3F4F75?logo=plotly&logoColor=white)](https://plotly.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.50+-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)


# Analysis_met

Расчет и визуализация прочностных характеристик стали.

### О проекте

В проекте представлена типовая задача обработки и визуализации результатов испытаний с использованием дашбордов.

### Данные

**Источник данных :** В данном проекте исходные данные синтетические, сгенерированные на основе нормального распределения с добавлением выбросов.

### Запуск тетради проекта

**Важно :** Перед запуском тетради убедитесь, что структура проекта сохранена.

## Приложение

**Приложение Streamlit :** https://analysismet-ifq4qmqptkqvrkylzyynwn.streamlit.app/

## Структура проекта

***Файлы проекта***
| Файл | Назначение |
|------------|------------|
| `app.py` | Streamlit приложение |
| `requirements.txt` | Зависимости |
| `README.md` | Этот файл |

***Данные : data/***
| Файл | Назначение |
|------------|------------|
| `metal_data.csv` | Файл исходных данных |

***Тетрадь проекта : notebook/***
| Файл | Назначение |
|------------|------------|
| `Analys_met.ipynb` | Jupyter ноутбук проекта |

***Изображения : image/***
| Файл | Назначение |
|------------|------------|
| `cylindrical_sample.png` | Тип образца |
| `table_d_d.png` | Допуски на размеры образцов |

***Страницы приложения : pages/***

| Файл | Назначение |
|------------|------------|
| `calculate_delta.py` | Расчет относительного удлинения |
| `calculate_psi.py` | Расчет относительного сужения |
| `calculate_sigma_b.py` | Расчет предела прочности |
| `check_emission_processing.py` | Проверка после предварительной обработки |
| `conclusions.py` | Выводы |
| `emission_processing.py` | Предварительная обработка данных |
| `input_data.py` | Исходные данные |
| `project.py` | Описание проекта |
| `thermins.py` | Термины и определения |
| `untils.py` | Обозначения и единицы измерения величин |


***Функции приложенния : utils/***
| Файл | Назначение |
|------------|------------|
| `calculations.py` | Расчетные функции |
| `constants.py` | Констранты |
| `data_processing.py` | Функция индексов отклонений размеров |
| `text_basis.py` | Текстовое описание результатов стат теста |
| `visualization.py` | Функции визуализации|


## Библитотеки и инструменты разработки

**Инструменты разработки**
- Jupyter Notebook
- Python 3.12.3

**Библиотеки**
- Numpy 1.26.4
- Pandas 2.2.2
- Scipy 1.13.1
- Plotly 5.24.1

**Визуализация**
- Streamlit 1.50.0
