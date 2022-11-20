Feature: Automation Practice browsing
    As a SDET
    I want to browse automationpractice website
    So that I can buy a product


Background:
    Given the automationpractice website is displayed

Scenario: ajouter connexion
    When l'utilisateur clique sur Configurer Connexion
    And il ajoute une nouvelle source de données "type conn" avec le port "100"
    Then verifier que la source de données "TEST_" est enregistrée
   Example:
   type conn / port
    Oracle     / 0
     MS/SQL       /100
