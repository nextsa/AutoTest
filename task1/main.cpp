//#include <QCoreApplication>
#include <iostream>
#include <ctime>

using std::cin;
using std::cout;
int main(int argc, char *argv[])
{
 //   QCoreApplication a(argc, argv);
    srand (time(NULL));

    int input = 0;
    cin >> input;

    int r = 0;
    r = rand() % 2 + 1;

    switch(input)
    {
    case 1:
        cout << "one";
        return 0;
    case 2:

        if (r == 1)
        {
            cout << "two";
        }
        else
        {
            cout << "toto";
        }

        break;
    default:
        cout << "undefined";
    }

  //  return a.exec();
}
