import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

# 1
def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_question_with_invalid_points():
    with pytest.raises(Exception):
        Question(title='q1', points=0)
    with pytest.raises(Exception):
        Question(title='q2', points=101)

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

# 2
def test_remove_choice_by_valid_id():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', True)

    question.remove_choice_by_id(1)
    assert len(question.choices) == 2
    
# 3
def test_remove_choice_by_invalid_id():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', True)
        
    with pytest.raises(Exception):
        question.remove_choice_by_id(4)

# 4
def test_remove_all_choices():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', True)
    
    question.remove_all_choices()
    assert len(question.choices) == 0

# 5
def test_set_correct_choices_valid_ids():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', False)

    question.set_correct_choices([1,3])
    assert question.choices[0].is_correct == True
    assert question.choices[1].is_correct == False
    assert question.choices[2].is_correct == True

# 6
def test_set_correct_choices_invalid_ids():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', False)

    with pytest.raises(Exception):
        question.set_correct_choices([1,4])

# 7
def test_correct_selected_choices_invalid_max_selections():
    question = Question(title='q1')
    question.add_choice('a', True)
    question.add_choice('b', False)
    question.add_choice('c', False)

    with pytest.raises(Exception):
        question.correct_selected_choices([1,3])

# 8
def test_correct_selected_choices_valid_id():
    question = Question(title='q1')
    question.add_choice('a', True)
    question.add_choice('b', False)
    question.add_choice('c', False)

    correct_selected_choices = question.correct_selected_choices([1])
    assert len(correct_selected_choices) == 1

# 9
def test_correct_selected_choices_invalid_id():
    question = Question(title='q1')
    question.add_choice('a', True)
    question.add_choice('b', False)
    question.add_choice('c', False)

    correct_selected_choices = question.correct_selected_choices([0])
    assert len(correct_selected_choices) == 0

# 10
def test_correct_selected_choices_wrong_answer():
    question = Question(title='q1')
    question.add_choice('a', True)
    question.add_choice('b', False)
    question.add_choice('c', False)

    correct_selected_choices = question.correct_selected_choices([2])
    assert len(correct_selected_choices) == 0