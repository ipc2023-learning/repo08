(define (problem strips-sat-x-1)
(:domain satellite)
(:objects
	satellite0 - satellite
	instrument0 - instrument
	instrument1 - instrument
	satellite1 - satellite
	instrument2 - instrument
	instrument3 - instrument
	instrument4 - instrument
	satellite2 - satellite
	instrument5 - instrument
	instrument6 - instrument
	instrument7 - instrument
	satellite3 - satellite
	instrument8 - instrument
	satellite4 - satellite
	instrument9 - instrument
	instrument10 - instrument
	instrument11 - instrument
	satellite5 - satellite
	instrument12 - instrument
	instrument13 - instrument
	satellite6 - satellite
	instrument14 - instrument
	instrument15 - instrument
	spectrograph0 - mode
	infrared1 - mode
	thermograph2 - mode
	GroundStation14 - direction
	Star30 - direction
	Star35 - direction
	Star0 - direction
	GroundStation10 - direction
	GroundStation34 - direction
	GroundStation16 - direction
	GroundStation27 - direction
	GroundStation21 - direction
	Star18 - direction
	GroundStation5 - direction
	Star28 - direction
	Star31 - direction
	GroundStation25 - direction
	GroundStation20 - direction
	GroundStation7 - direction
	Star29 - direction
	GroundStation9 - direction
	Star33 - direction
	GroundStation11 - direction
	GroundStation6 - direction
	Star24 - direction
	Star13 - direction
	GroundStation4 - direction
	Star15 - direction
	GroundStation3 - direction
	Star37 - direction
	Star38 - direction
	Star19 - direction
	Star36 - direction
	Star26 - direction
	Star2 - direction
	Star32 - direction
	GroundStation23 - direction
	Star12 - direction
	Star8 - direction
	Star17 - direction
	GroundStation1 - direction
	Star22 - direction
	Star39 - direction
	Planet40 - direction
	Phenomenon41 - direction
	Star42 - direction
	Star43 - direction
	Phenomenon44 - direction
	Star45 - direction
	Planet46 - direction
	Star47 - direction
	Star48 - direction
)
(:init
	(supports instrument0 infrared1)
	(supports instrument0 spectrograph0)
	(supports instrument0 thermograph2)
	(calibration_target instrument0 Star2)
	(calibration_target instrument0 Star13)
	(calibration_target instrument0 Star24)
	(calibration_target instrument0 GroundStation21)
	(calibration_target instrument0 Star8)
	(calibration_target instrument0 GroundStation10)
	(calibration_target instrument0 Star32)
	(calibration_target instrument0 Star38)
	(calibration_target instrument0 GroundStation11)
	(calibration_target instrument0 Star12)
	(supports instrument1 thermograph2)
	(calibration_target instrument1 GroundStation9)
	(calibration_target instrument1 GroundStation25)
	(calibration_target instrument1 Star24)
	(calibration_target instrument1 GroundStation7)
	(calibration_target instrument1 GroundStation1)
	(calibration_target instrument1 Star29)
	(calibration_target instrument1 Star31)
	(calibration_target instrument1 Star12)
	(on_board instrument0 satellite0)
	(on_board instrument1 satellite0)
	(power_avail satellite0)
	(pointing satellite0 GroundStation4)
	(supports instrument2 infrared1)
	(supports instrument2 thermograph2)
	(calibration_target instrument2 Star37)
	(calibration_target instrument2 GroundStation4)
	(calibration_target instrument2 GroundStation5)
	(calibration_target instrument2 GroundStation16)
	(calibration_target instrument2 Star22)
	(calibration_target instrument2 Star36)
	(calibration_target instrument2 GroundStation6)
	(calibration_target instrument2 GroundStation34)
	(calibration_target instrument2 Star38)
	(calibration_target instrument2 GroundStation10)
	(calibration_target instrument2 Star0)
	(supports instrument3 thermograph2)
	(supports instrument3 infrared1)
	(supports instrument3 spectrograph0)
	(calibration_target instrument3 GroundStation11)
	(calibration_target instrument3 Star36)
	(calibration_target instrument3 GroundStation21)
	(calibration_target instrument3 GroundStation20)
	(calibration_target instrument3 Star13)
	(calibration_target instrument3 Star31)
	(calibration_target instrument3 GroundStation27)
	(supports instrument4 infrared1)
	(calibration_target instrument4 Star19)
	(calibration_target instrument4 Star28)
	(calibration_target instrument4 GroundStation5)
	(calibration_target instrument4 Star18)
	(calibration_target instrument4 Star29)
	(calibration_target instrument4 GroundStation21)
	(on_board instrument2 satellite1)
	(on_board instrument3 satellite1)
	(on_board instrument4 satellite1)
	(power_avail satellite1)
	(pointing satellite1 Planet40)
	(supports instrument5 infrared1)
	(supports instrument5 spectrograph0)
	(calibration_target instrument5 Star31)
	(calibration_target instrument5 GroundStation3)
	(calibration_target instrument5 GroundStation6)
	(calibration_target instrument5 Star17)
	(calibration_target instrument5 Star12)
	(supports instrument6 thermograph2)
	(supports instrument6 spectrograph0)
	(calibration_target instrument6 GroundStation7)
	(calibration_target instrument6 GroundStation20)
	(calibration_target instrument6 Star36)
	(calibration_target instrument6 GroundStation25)
	(calibration_target instrument6 Star29)
	(calibration_target instrument6 Star19)
	(supports instrument7 thermograph2)
	(supports instrument7 infrared1)
	(supports instrument7 spectrograph0)
	(calibration_target instrument7 GroundStation3)
	(calibration_target instrument7 Star32)
	(calibration_target instrument7 Star29)
	(calibration_target instrument7 Star19)
	(on_board instrument5 satellite2)
	(on_board instrument6 satellite2)
	(on_board instrument7 satellite2)
	(power_avail satellite2)
	(pointing satellite2 Star22)
	(supports instrument8 thermograph2)
	(calibration_target instrument8 Star32)
	(calibration_target instrument8 GroundStation11)
	(calibration_target instrument8 Star33)
	(calibration_target instrument8 GroundStation9)
	(calibration_target instrument8 Star29)
	(on_board instrument8 satellite3)
	(power_avail satellite3)
	(pointing satellite3 Star38)
	(supports instrument9 infrared1)
	(supports instrument9 spectrograph0)
	(supports instrument9 thermograph2)
	(calibration_target instrument9 GroundStation6)
	(calibration_target instrument9 GroundStation3)
	(supports instrument10 infrared1)
	(supports instrument10 spectrograph0)
	(supports instrument10 thermograph2)
	(calibration_target instrument10 Star13)
	(calibration_target instrument10 Star24)
	(calibration_target instrument10 Star22)
	(supports instrument11 thermograph2)
	(supports instrument11 infrared1)
	(calibration_target instrument11 GroundStation4)
	(calibration_target instrument11 Star13)
	(on_board instrument9 satellite4)
	(on_board instrument10 satellite4)
	(on_board instrument11 satellite4)
	(power_avail satellite4)
	(pointing satellite4 Star0)
	(supports instrument12 spectrograph0)
	(supports instrument12 infrared1)
	(calibration_target instrument12 Star38)
	(calibration_target instrument12 Star37)
	(calibration_target instrument12 Star8)
	(calibration_target instrument12 GroundStation3)
	(calibration_target instrument12 Star15)
	(supports instrument13 infrared1)
	(supports instrument13 spectrograph0)
	(calibration_target instrument13 GroundStation23)
	(calibration_target instrument13 Star32)
	(calibration_target instrument13 Star2)
	(calibration_target instrument13 Star26)
	(calibration_target instrument13 Star22)
	(calibration_target instrument13 Star12)
	(calibration_target instrument13 Star36)
	(calibration_target instrument13 Star19)
	(calibration_target instrument13 Star17)
	(calibration_target instrument13 Star8)
	(on_board instrument12 satellite5)
	(on_board instrument13 satellite5)
	(power_avail satellite5)
	(pointing satellite5 Star32)
	(supports instrument14 thermograph2)
	(calibration_target instrument14 Star12)
	(supports instrument15 thermograph2)
	(supports instrument15 spectrograph0)
	(supports instrument15 infrared1)
	(calibration_target instrument15 Star22)
	(calibration_target instrument15 GroundStation1)
	(calibration_target instrument15 Star17)
	(calibration_target instrument15 Star8)
	(calibration_target instrument15 Star12)
	(on_board instrument14 satellite6)
	(on_board instrument15 satellite6)
	(power_avail satellite6)
	(pointing satellite6 Star42)
)
(:goal (and
	(pointing satellite0 Star43)
	(pointing satellite2 Star12)
	(pointing satellite5 GroundStation21)
	(have_image Star39 infrared1)
	(have_image Planet40 spectrograph0)
	(have_image Phenomenon41 thermograph2)
	(have_image Star42 spectrograph0)
	(have_image Star43 infrared1)
	(have_image Phenomenon44 spectrograph0)
	(have_image Star45 thermograph2)
	(have_image Planet46 spectrograph0)
	(have_image Star47 infrared1)
	(have_image Star48 spectrograph0)
))

)
