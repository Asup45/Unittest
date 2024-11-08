def test_sklearn_classifier(self):
        self._test_classifier(self.sklearn_classifier)
 
    def _test_classifier(self, classifier):
        classifier.fit(self.X_train, self.y_train)
        y_pred = classifier.predict(self.X_test)
 
        # Assertion tests
        self.assertTrue(confusion_matrix(self.y_test, y_pred) is not None)
        self.assertTrue(classification_report(self.y_test, y_pred) is not None)
 
    def test_learning_curve(self):
        self._test_learning_curve(self.sklearn_classifier)
 
    def _test_learning_curve(self, classifier):
        N, train_score, val_score = learning_curve(
            classifier, self.X_train, self.y_train, cv=4, scoring='f1', train_sizes=np.linspace(0.1, 1, num=10)
        )
 
        # Assertion tests
        self.assertTrue(N is not None)
        self.assertTrue(train_score is not None)
        self.assertTrue(val_score is not None)