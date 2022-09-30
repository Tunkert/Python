from feature import copyright
import feature.subfeature.number_methods as numbmeth

package_name = "package"

print("The copyright date of this package is " + str(copyright.date_of_copyright))
print("The creator of this package is " + numbmeth.creator + ".")
