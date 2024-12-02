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

    def test_add_new_book_symbols_more_41(self, collector):
        collector.add_new_book('Тушеные оранжевые огурцы в кафе "Весь станок')
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_set_horrors(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_book_genre_get_detective(self, collector):
        collector.add_new_book('Что делать, когда не знаешь что делать')
        collector.set_book_genre('Что делать, когда не знаешь что делать', 'Детективы')

        assert collector.books_genre.get('Что делать, когда не знаешь что делать') == 'Детективы'

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Что делать, когда не знаешь что делать', 'Детективы'],
            ['Гордость и предубеждение и зомби', 'Ужасы'],
            ['Пособие по взрослой жизни', 'Ужасы']
        ]
    )

    def test_get_books_with_specific_genre_get_horrors(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        list_names_horrors = []
        for i in name, genre:
            horrors_book = collector.get_books_with_specific_genre('Ужасы')
            list_names_horrors.append(horrors_book)

        assert len(list_names_horrors) == 2


    def test_get_books_genre(self, collector):
        list_of_books = ['Что делать, когда не знаешь что делать', 'Гордость и предубеждение и зомби', 'Пособие по взрослой жизни']
        for i in list_of_books:
            collector.add_new_book(i)
        assert len(collector.get_books_genre()) == 3

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Алиса в стране', 'Комедии'],
            ['Том и Джерри и еще Том', 'Мультфильмы'],
            ['Пособие по взрослой жизни', 'Ужасы']
        ]
    )
    def test_get_books_for_children_with_valid_book(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        list_names_for_children = []
        for i in name, genre:
            child_books = collector.get_books_for_children()
            list_names_for_children.append(child_books)
        assert len(list_names_for_children) == 2

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

