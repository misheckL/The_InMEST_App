import 'package:flutter/material.dart';
import 'package:tontineo_app/tontineo_home_page.dart';

import 'package:tontineo_app/l10n/app_localizations.dart'; // Adjust the import path

void main() async {
  runApp(const TontineoApp());
}

class TontineoApp extends StatelessWidget {
  const TontineoApp({super.key}); // Correct the syntax for the constructor

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      localizationsDelegates: [ // Add this line
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
      ],
      supportedLocales: [
        const Locale('en', ''), // English
        const Locale('es', ''), // Spanish
        const Locale('fr', ''), // French
        // Add more supported locales as needed
      ],
      home:
          TontineoHomePage(), // Replace TontineoAppHome() with your actual home page
    );
  }
}

class GlobalWidgetsLocalizations {}

class GlobalMaterialLocalizations {}

class AppLocalizationsDelegate
    extends LocalizationsDelegate<AppLocalizationsDelegate> {
  const AppLocalizationsDelegate();

  @override
  bool isSupported(Locale locale) {
    // Update the list to include all the supported locales
    return ['en', 'es', 'fr'].contains(locale.languageCode);
  }

  @override
  Future<AppLocalizations> load(Locale locale) {
    return AppLocalizations.load(locale);
  }

  @override
  bool shouldReload(covariant LocalizationsDelegate<AppLocalizations> old) {
    return false;
  }
}

class AppLocalizations {
}
