var fieldsToValidate = document.querySelectorAll('[data-validators]')
for (fieldToValidate of fieldsToValidate) {
  fieldToValidate.oninput = function() {
    var fieldValidators = eval(this.attributes['data-validators'].value)
    var failingValidators = []
    for (validatorFunction of fieldValidators) {
      try {
        validatorFunction(this.value)
      }
      catch(e) {
        this.setCustomValidity(e.message)
        failingValidators.push(validatorFunction)
      }
    }
    if (failingValidators.length === 0) {
      this.setCustomValidity('')
    }
  }
}
