#include <QString>
#include <QtTest>

class Untitled2Test : public QObject
{
    Q_OBJECT

public:
    Untitled2Test();

private Q_SLOTS:
    void testCase1();
};

Untitled2Test::Untitled2Test()
{
}

void Untitled2Test::testCase1()
{
    QVERIFY2(true, "Failure");
}

QTEST_APPLESS_MAIN(Untitled2Test)

#include "tst_untitled2test.moc"
