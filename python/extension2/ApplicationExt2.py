from python.root.CashDesk import CashDesk
from python.root.CoffeeHouse import CoffeeHouse
from python.root.Ingredient import Ingredient
from python.root.KitchenMachine import KitchenMachine
from python.root.Product import Product
from python.root.Recipe import Recipe
from python.root.RecipeStep import RecipeStep
from python.extension2.VisitorGeneratorExt2 import VisitorGeneratorExt2
from python.root.Worker import Worker


class ApplicationExt2:
    @staticmethod
    def build() -> CoffeeHouse:
        model = CoffeeHouse()
        model.setVisitorGenerator(VisitorGeneratorExt2(model))

        cashDesk = CashDesk()
        cashDesk.setWorker(Worker(model, cashDesk))
        model.addCashDesk(cashDesk)

        cashDesk = CashDesk()
        cashDesk.setWorker(Worker(model, cashDesk))
        model.addCashDesk(cashDesk)

        model.addDessert(Product("Печенье", False), 20)
        model.addDessert(Product("Пирожное", False), 20)
        model.addDessert(Product("Торт", False), 20)

        coffeeBeans = Ingredient("Кофейные зерна")
        milk = Ingredient("Молоко")
        syrup = Ingredient("Сироп")

        model.addIngredient(coffeeBeans, 1000)
        model.addIngredient(milk, 200)
        model.addIngredient(syrup, 100)

        coffeeMachine = KitchenMachine("Кофе машина")
        cappuccinatore = KitchenMachine("Капучинатор")

        model.addRecipe(Product('Эспрессо', True), Recipe().addStep(RecipeStep(coffeeBeans, 5, coffeeMachine, 120)))
        model.addRecipe(Product('Раф кофе', True), Recipe()
                        .addStep(RecipeStep(syrup, 10, None, 10))
                        .addStep(RecipeStep(coffeeBeans, 5, coffeeMachine, 120))
                        .addStep(RecipeStep(milk, 10, cappuccinatore, 100))
                        )
        model.addRecipe(Product('Каппучино', True), Recipe()
                        .addStep(RecipeStep(coffeeBeans, 5, coffeeMachine, 120))
                        .addStep(RecipeStep(milk, 10, None, 10))
                        .addStep(RecipeStep(milk, 10, cappuccinatore, 100))
                        )

        return model
