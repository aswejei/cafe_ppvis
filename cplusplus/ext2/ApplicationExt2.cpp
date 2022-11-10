#include "ApplicationExt2.hpp"

ApplicationExt2::ApplicationExt2()
{
}

CoffeeHouse *ApplicationExt2::build()
{
	CoffeeHouse *model = new CoffeeHouse();
	model->setVisitorGenerator(new VisitorGeneratorExt2(model));

	CashDesk *cashDesk = new CashDesk();
	cashDesk->setWorker(new Worker(model, cashDesk));
	model->addCashDesk(cashDesk);

	cashDesk = new CashDesk();
	cashDesk->setWorker(new Worker(model, cashDesk));
	model->addCashDesk(cashDesk);

	model->addDessert(new Product("Печенье", false), 20);
	model->addDessert(new Product("Пирожное", false), 20);
	model->addDessert(new Product("Торт", false), 20);

	Ingredient *coffeeBeans = new Ingredient("Кофейные зерна");
	Ingredient *milk = new Ingredient("Молоко");
	Ingredient *syrup = new Ingredient("Сироп");

	model->addIngredient(coffeeBeans, 1000);
	model->addIngredient(milk, 200);
	model->addIngredient(syrup, 100);

	KitchenMachine *coffeeMachine = new KitchenMachine("Кофе машина");
	KitchenMachine *cappuccinatore = new KitchenMachine("Капучинатор");

	model->addRecipe(new Product("Эспрессо", true),
		(new Recipe())
		->addStep(new RecipeStep(coffeeBeans, 5, coffeeMachine, 120)));
	model->addRecipe(new Product("Раф кофе", true),
		(new Recipe())
		->addStep(new RecipeStep(syrup, 10, nullptr, 10))
		->addStep(new RecipeStep(coffeeBeans, 5, coffeeMachine, 120))
		->addStep(new RecipeStep(milk, 10, cappuccinatore, 100)));
	model->addRecipe(new Product("Каппучино", true),
		(new Recipe())
		->addStep(new RecipeStep(coffeeBeans, 5, coffeeMachine, 120))
		->addStep(new RecipeStep(milk, 10, nullptr, 10))
		->addStep(new RecipeStep(milk, 10, cappuccinatore, 100)));

	return model;
}
