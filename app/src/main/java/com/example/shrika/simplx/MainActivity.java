package com.example.shrika.simplx;

import android.animation.Animator;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.res.AssetManager;
import android.graphics.Color;
import android.graphics.Typeface;
import android.graphics.drawable.ColorDrawable;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewAnimationUtils;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.FrameLayout;
import android.widget.TextView;

import java.util.Locale;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN);
        getSupportActionBar().hide();
        setContentView(R.layout.activity_main);

        AssetManager am = getApplicationContext().getAssets();
        Typeface custom = Typeface.createFromAsset(am,
                String.format(Locale.US, "fonts/%s", "Kelvetica.otf"));
        final Button bAlg = (Button) findViewById(R.id.bAlg);
        final Button bflow = (Button) findViewById(R.id.bflow);
        bAlg.setTypeface(custom);
        bflow.setTypeface(custom);
    }
    public void algClick(View v){
        LayoutInflater inflater = getLayoutInflater();
        final View alertLayout = inflater.inflate(R.layout.language_sel, null);
        AlertDialog.Builder alert = new AlertDialog.Builder(this);
        alert.setView(alertLayout);
        alert.setCancelable(true);
        AlertDialog dialog = alert.create();
        dialog.setOnShowListener(new DialogInterface.OnShowListener() {
            @Override public void onShow(DialogInterface dialog) {
                AlertDialog alertDialog = (AlertDialog) dialog;
                View view = alertDialog.getWindow().getDecorView()
                        .findViewById(android.R.id.content);
                FrameLayout.LayoutParams layoutParams = (FrameLayout.LayoutParams) view.getLayoutParams();
                layoutParams.width = 4 * alertLayout.getWidth() / 5; // 80% of screen
                layoutParams.gravity = Gravity.CENTER;
                view.setLayoutParams(layoutParams);
                alertDialog.getWindow().setBackgroundDrawable(
                        new ColorDrawable(Color.TRANSPARENT));
                int centerX = alertLayout.getWidth() / 2;
                int centerY = alertLayout.getHeight() / 2;
                float startRadius = 20;
                float endRadius = alertLayout.getHeight();
                Animator animator = ViewAnimationUtils.createCircularReveal(alertLayout, centerX, centerY, startRadius, endRadius);
                animator.setDuration(1000);
                animator.start();
            }
        });
        dialog.show();
    }

    public void flowClick(View v){
        LayoutInflater inflater = getLayoutInflater();
        final View alertLayout = inflater.inflate(R.layout.language_sel, null);
        AlertDialog.Builder alert = new AlertDialog.Builder(this);
        alert.setView(alertLayout);
        alert.setCancelable(true);
        AlertDialog dialog = alert.create();
        dialog.setOnShowListener(new DialogInterface.OnShowListener() {
            @Override public void onShow(DialogInterface dialog) {
                AlertDialog alertDialog = (AlertDialog) dialog;
                View view = alertDialog.getWindow().getDecorView()
                        .findViewById(android.R.id.content);
                FrameLayout.LayoutParams layoutParams = (FrameLayout.LayoutParams) view.getLayoutParams();
                layoutParams.width = 4 * alertLayout.getWidth() / 5; // 80% of screen
                layoutParams.gravity = Gravity.CENTER;
                view.setLayoutParams(layoutParams);
                alertDialog.getWindow().setBackgroundDrawable(
                        new ColorDrawable(Color.TRANSPARENT));
                int centerX = alertLayout.getWidth() / 2;
                int centerY = alertLayout.getHeight() / 2;
                float startRadius = 20;
                float endRadius = alertLayout.getHeight();
                Animator animator = ViewAnimationUtils.createCircularReveal(alertLayout, centerX, centerY, startRadius, endRadius);
                animator.setDuration(1000);
                animator.start();
            }
        });
        dialog.show();
    }
}
