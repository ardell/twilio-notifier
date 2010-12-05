<?php

$spec = Pearfarm_PackageSpec::create(array(Pearfarm_PackageSpec::OPT_BASEDIR => dirname(__FILE__)))
             ->setName('twilioNotifier')
             ->setChannel('ardell.pearfarm.org')
             ->setSummary('A notifier for Twilio.')
             ->setDescription('A command to pull down notifications from your Twilio log and email them to you.')
             ->addPackageDependency('climax', 'apinstein.pearfarm.org')
             ->setReleaseVersion('0.0.1')
             ->setReleaseStability('alpha')
             ->setApiVersion('0.0.1')
             ->setApiStability('alpha')
             ->setLicense(Pearfarm_PackageSpec::LICENSE_MIT)
             ->setNotes('Initial release.')
             ->addMaintainer('lead', 'Jason Ardell', 'ardell', 'ardell@gmail.com')
             ->addGitFiles()
             ;
