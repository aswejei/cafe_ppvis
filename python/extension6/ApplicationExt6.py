from python.extension6.CoffeeHouseWithSupplyManager import CoffeeHouseWithSupplyManager
from python.extension6.SupplyManager import SupplyManager
from python.root.CashDesk import CashDesk
from python.root.Ingredient import Ingredient
from python.root.KitchenMachine import KitchenMachine
from python.root.Product import Product
from python.root.Recipe import Recipe
from python.root.RecipeStep import RecipeStep
from python.root.VisitorGenerator import VisitorGenerator
from python.root.Worker import Worker


class ApplicationExt6:
    @staticmethod
    def build() -> CoffeeHouseWithSupplyManager:
        model = CoffeeHouseWithSupplyManager()

        model.setVisitorGenerator(VisitorGenerator(model))

        cashDesk = CashDesk()
        cashDesk.setWorker(Worker(model, cashDesk))
        model.addCashDesk(cashDesk)

        cashDesk = CashDesk()
        cashDesk.setWorker(Worker(model, cashDesk))
        model.addCashDesk(cashDesk)

        model.addSupplyManager(SupplyManager(model))

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