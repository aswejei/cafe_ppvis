from extension6.ApplicationExt6 import ApplicationExt6

if __name__ == '__main__':
    model = ApplicationExt6.build()
    print('Start modelling')
    model.run()
    print(f'Finish rating: {model.getAvgRating()}')