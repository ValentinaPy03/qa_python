from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize(
        'invalid_name',
        [
            'Тушеные оранжевые огурцы в кафе "Весь станок"',
            '',
            'Гордость и предубеждение и зомби'
        ]
    )
    def test_add_new_book_invalid_name(self, collector, invalid_name):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book(invalid_name)
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_set_horrors(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби':'Ужасы'}

    def test_get_book_genre_get_detective(self, collector):
        collector.add_new_book('Что делать, когда не знаешь что делать')
        collector.set_book_genre('Что делать, когда не знаешь что делать', 'Детективы')
        assert collector.get_book_genre('Что делать, когда не знаешь что делать') == 'Детективы'

    def test_get_books_with_specific_genre_get_horrors(self, collector):
        books_name = ['Что делать, когда не знаешь что делать', 'Гордость и предубеждение и зомби', 'Пособие по взрослой жизни']
        for book_name in books_name:
            collector.add_new_book(book_name)
        collector.set_book_genre('Что делать, когда не знаешь что делать', 'Детективы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Пособие по взрослой жизни', 'Ужасы')
        horrors_book = collector.get_books_with_specific_genre('Ужасы')
        assert len(horrors_book) == 2

    def test_get_books_genre(self, collector):
        list_of_books = ['Что делать, когда не знаешь что делать', 'Гордость и предубеждение и зомби', 'Пособие по взрослой жизни']
        for i in list_of_books:
            collector.add_new_book(i)
        assert len(collector.get_books_genre()) == 3

    def test_get_books_for_children_with_valid_book(self, collector):
        books_name = ['Алиса в стране', 'Том и Джерри и еще Том', 'Пособие по взрослой жизни']
        for book_name in books_name:
            collector.add_new_book(book_name)
        collector.set_book_genre('Алиса в стране', 'Комедии')
        collector.set_book_genre('Том и Джерри и еще Том', 'Мультфильмы')
        collector.set_book_genre('Пособие по взрослой жизни', 'Ужасы')
        child_books = collector.get_books_for_children()
        assert len(child_books) == 2

    def test_add_book_in_favorites_new_book(self, collector):
        collector.add_new_book('Алиса в стране')
        collector.add_book_in_favorites('Алиса в стране')
        assert len(collector.favorites) == 1

    def test_add_book_in_favorites_old_book(self, collector):
        collector.add_new_book('Алиса в стране')
        collector.add_book_in_favorites('Алиса в стране')
        collector.add_book_in_favorites('Алиса в стране')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Алиса в стране')
        collector.add_book_in_favorites('Алиса в стране')
        collector.delete_book_from_favorites('Алиса в стране')
        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books(self, collector):
        list_fav = ['Алиса в стране', 'Том и Джерри и еще Том', 'Пособие по взрослой жизни', 'Гордость и предубеждение и зомби', 'Азбука']
        for i in list_fav:
            collector.add_new_book(i)
            collector.add_book_in_favorites(i)
        assert len(collector.get_list_of_favorites_books()) == 5

