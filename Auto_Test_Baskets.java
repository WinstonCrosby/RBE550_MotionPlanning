package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.Autonomous;
import com.qualcomm.robotcore.eventloop.opmode.OpMode;
import com.qualcomm.robotcore.hardware.CRServo;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.Servo;
import com.qualcomm.robotcore.util.ElapsedTime;

@Autonomous
public class Auto_Test_Baskets extends OpMode {

    DcMotor motorFL;
    DcMotor motorFR;
    DcMotor motorBL;
    DcMotor motorBR;
    DcMotor ArmMotor;
    CRServo grabber;
    Servo wrist;


    double up = 1930;
    double preErr = 0;
    ElapsedTime timer = new ElapsedTime();


    @Override
    public void init() {
        motorFL = hardwareMap.get(DcMotor.class, "motorFL");
        motorFR = hardwareMap.get(DcMotor.class, "motorFR");
        motorBL = hardwareMap.get(DcMotor.class, "motorBL");
        motorBR = hardwareMap.get(DcMotor.class, "motorBR");
        ArmMotor = hardwareMap.get(DcMotor.class, "ArmMotor");
        ArmMotor.setZeroPowerBehavior(DcMotor.ZeroPowerBehavior.BRAKE);
        grabber = hardwareMap.get(CRServo.class, "grabber");

    }

    @Override
    public void start() {

        timer.reset();
        while (timer.seconds() < 1.5) {

            motorFL.setPower(-0.30);
            motorFR.setPower(0.30);
            motorBL.setPower(-0.30);
            motorBR.setPower(0.30);

        }

        motorFL.setPower(0);
        motorFR.setPower(0);
        motorBL.setPower(0);
        motorBR.setPower(0);

        timer.reset();
        while (timer.seconds() < 7) {
            double setVal = ArmMotor.getCurrentPosition();
            double ep = up - setVal;

            double p = 0.0005;
            double d = 0.0005;

            double ed = ep - preErr;
            preErr = ep;

            double UP = (p * ep) + (d * ed);
            ArmMotor.setPower(UP);

            /*while (timer.seconds() > 5){
                wrist.setPosition(0.39);
            }*/

            while (timer.seconds() > 6 && timer.seconds() < 7) {
                grabber.setPower(1);
            }
        }


        ArmMotor.setPower(0);
        grabber.setPower(0);
        timer.reset();

        while (timer.seconds() < 0.5){
            motorFL.setPower(0.30);
            motorFR.setPower(-0.30);
            motorBL.setPower(0.30);
            motorBR.setPower(-0.30);
        }
        timer.reset();

        while (timer.seconds() < 3){
            motorFL.setPower(-0.35);
            motorFR.setPower(-0.30);
            motorBL.setPower(0.30);
            motorBR.setPower(0.35);
        }
        motorFL.setPower(0);
        motorFR.setPower(0);
        motorBL.setPower(0);
        motorBR.setPower(0);
        timer.reset();

    }

    public void loop() {}

}