# kualitee

Use below command to run the feature file without reporting
behave Integration_Module/features/kualitee.feature

Use below command to generate allure report.
behave -f allure_behave.formatter:AllureFormatter -o reports/ .\Integration_Module\features\kualitee.feature

Use Below command to see Allure Report.
allure serve reports/
