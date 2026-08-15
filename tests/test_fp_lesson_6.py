import io
import unittest
from contextlib import redirect_stdout

from pymonad.state import State

from fp_lesson_6 import create_route, main, walk


class StateLessonTest(unittest.TestCase):
    def test_walk_adds_place_and_steps(self):
        result = walk("Парк", 1200)(["Дом"]).run(300)

        self.assertEqual(result, (["Дом", "Парк"], 1500))

    def test_walk_does_not_mutate_input_list(self):
        visited_places = ["Дом"]

        walk("Парк", 1200)(visited_places).run(300)

        self.assertEqual(visited_places, ["Дом"])

    def test_route_returns_places_and_total_steps(self):
        self.assertEqual(
            create_route().run(0),
            (["Дом", "Парк", "Магазин"], 3500),
        )

    def test_route_is_deferred_and_can_use_another_initial_state(self):
        route = create_route()

        self.assertIsInstance(route, State)
        self.assertEqual(
            route.run(100),
            (["Дом", "Парк", "Магазин"], 3600),
        )

    def test_main_prints_route_and_steps(self):
        output = io.StringIO()

        with redirect_stdout(output):
            main()

        self.assertEqual(output.getvalue().splitlines(), [
            "Маршрут: Дом -> Парк -> Магазин",
            "Всего шагов: 3500",
        ])


if __name__ == "__main__":
    unittest.main()
