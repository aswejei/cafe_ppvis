from root.Application import Application

if __name__ == '__main__':
    model = Application.build()
    print('Start modelling')
    model.run()
    print(f'Finish rating: {model.getAvgRating()}')
