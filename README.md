# CFE_Try-Django-1.11

[codingforentrepreneurs.com](https://www.codingforentrepreneurs.com/projects/try-django-111/)
### Python Version: 3.6.0


## 프로젝트명: Yelp와 유사한 음식점 소개 web application 만들기

#### 목적: Django 1.11의 전반적인 기본 개념 실습

## 의의
### django 실전 project 예제들로 유명한 [codingforentrepreneurs.com](https://www.codingforentrepreneurs.com/projects/try-django-111/)의 강사님이 설명해주시는, 일반적>    인 django project에서 필요한 전반적인 개념 및 팁 공부 및 실습


## 공부한 내용

### 1. Signals - pre_save, post_save
### 2. unique_slug_generator
### 3. Forms and Validation
#### 3-1) forms, model forms (forms.py)
* #####  `clean_field()`, `clean()` methods
##### form.errors, form.errors.non_field_errors(for example, errors raised in `clean()` method)
#### 3-2) CBV; CreateView
#### 3-3) Custom Validators (validators.py)
##### * you can put custom validators in fields in forms.py or models.py
##### * Validators only validate, they don't return the improved format; Clean methods both validate and return a (sometimes amended) value
##### * validors just validate things, if you want to change the field value, use pre_save signals
