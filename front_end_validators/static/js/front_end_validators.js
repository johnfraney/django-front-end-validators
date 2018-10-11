var fieldsToValidate = document.querySelectorAll('[data-validators]')
for (fieldToValidate of fieldsToValidate) {
  fieldToValidate.oninput = function() {
    var fieldValidators = eval(this.attributes['data-validators'].value)
    for (validatorFunction of fieldValidators) {
      try {
        validatorFunction(this.value)
        var fieldIsValid = this.checkValidity()
        if (fieldIsValid) {
          this.setCustomValidity('')
        }
      }
      catch(e) {
        this.setCustomValidity(e.message)
      }
    }
  }
}
