describe('Accounts test', () => {

    it('user can rgister new account, log in and navigate to /account', () => {
        cy.visit('/');
        cy.get('.nav-btn-register').click();
        cy.get('.input-username').type('cyTestAccounts');
        cy.get('.input-email').type('cy_test_accounts@trackerrr.com');
        cy.get('.input-password').type('test4321');
        cy.get('.input-password2').type('test4321');
        cy.get('.btn-register-submit').click();
        cy.contains('Account has been created');

        cy.visit('/');
        cy.contains('h1', 'Time tracker');
        cy.get('.nav-btn-login').click();
        cy.get('.input-username').type('cyTestAccounts');
        cy.get('.input-password').type('test4321');
        cy.get('.btn-login-submit').click();
        cy.url().should('include', 'tracker');
        cy.get('[href="/account"]').click()
    });

    it('registaration email is visible to the user', () => {
        cy.contains('cy_test_accounts@trackerrr.com')
    });

    it('the user can not change password if the old password is incorrect', () => {
        cy.get('.cy-input-old-password').type('incorrect_password123')
        cy.get('.cy-input-password').type('new_pass_321')
        cy.get('.cy-input-password2').type('new_pass_321')
        cy.get('.btn-change-password').click()
        cy.contains('Please retype your current password.')
    })

    it('the user can change password', () => {
        cy.get('.cy-input-old-password').type('test4321')
        cy.get('.cy-input-password').type('new_pass_321')
        cy.get('.cy-input-password2').type('new_pass_321')
        cy.get('.btn-change-password').click()
        cy.contains('Password successfully updated')
        
        cy.get('.nav-btn-logout').click()
        cy.get('body').should('not.contain', 'Account')
    })

    it('the user can log in using changed password', () => {
        cy.visit('/');
        cy.contains('h1', 'Time tracker');
        cy.get('.nav-btn-login').click();
        cy.get('.input-username').type('cyTestAccounts');
        cy.get('.input-password').type('new_pass_321');
        cy.get('.btn-login-submit').click();
        cy.url().should('include', 'tracker');
    })
});