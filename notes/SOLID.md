# SOLID

Solid Principles are use to make enterpises level software architecture.

## 1. S -> Single Responsibility Principle (SRP)

- Split the code by reason to change, not just by "related functionality"
- every class should perform/handel single reponsibility

## 2. O -> Open / Close Principle (OCP)

- A class should be open for extension, closed for modifications
- common interface, new implementations

## 3. L -> Liskov Substitution Principle (LSP)

- If B is a subclass of A, you should be able to use B anywhere A is expected without the caller noticing anything broke
- typical violations
  - Return a different type / shape then the base class
  - Throws new exceptions the caller never expected
  - Silently does less than what base class can

## 4. I -> Intreface Segregation Principle (ISP)

- No class should be forces to depend on method it doesn't use
- basically a class should only implements what it does.

## 5. D -> Dependency Inversion Principle (DIP)

- Higher level modeules shouldn't depends on lower level modules, both should depend on abstraction
- make the lower lever & higher level swappable
