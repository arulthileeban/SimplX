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
import android.widget.Toast;

import java.io.IOException;
import java.util.Locale;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Response;

public class MainActivity extends AppCompatActivity {

    private final OkHttpClient client = new OkHttpClient();
    String respdata="";

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

        AssetManager am = getApplicationContext().getAssets();
        Typeface custom = Typeface.createFromAsset(am,
                String.format(Locale.US, "fonts/%s", "Kelvetica.otf"));
        Button r1 = (Button)alertLayout.findViewById(R.id.r1);
        Button r2 = (Button)alertLayout.findViewById(R.id.r2);
        Button r3 = (Button)alertLayout.findViewById(R.id.r3);
        TextView txt = (TextView)alertLayout.findViewById(R.id.alertalgflow);
        txt.setTypeface(custom);
        r1.setTypeface(custom);
        r2.setTypeface(custom);
        r3.setTypeface(custom);
        txt.setText("Algorithm");
        r1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
                    String url = "http://ec2-52-36-236-91.us-west-2.compute.amazonaws.com:5000/language?lang="+"cpp";
                    run(url);
                    Thread thread1 = new Thread(new Runnable(){
                        @Override
                        public void run(){
                            while (respdata.equals("")){}
                            runOnUiThread(new Runnable() {
                                @Override
                                public void run() {

                                    Intent algo = new Intent(MainActivity.this, algorithm.class);
                                    algo.putExtra("type", "c++");
                                    startActivity(algo);

                                }
                            });


                        }
                    });
                    thread1.start();
                }catch (Exception e){

                }
            }
        });
        r2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                try {
                    String url = "http://ec2-52-36-236-91.us-west-2.compute.amazonaws.com:5000/language?lang="+"Python";
                    run(url);
                    Thread thread1 = new Thread(new Runnable(){
                        @Override
                        public void run(){
                            while (respdata.equals("")){}
                            runOnUiThread(new Runnable() {
                                @Override
                                public void run() {

                                    Intent algo = new Intent(MainActivity.this, algorithm.class);
                                    algo.putExtra("type", "python");
                                    startActivity(algo);

                                }
                            });


                        }
                    });
                    thread1.start();
                }catch (Exception e){

                }
            }
        });
        r3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {try {
                String url = "http://ec2-52-36-236-91.us-west-2.compute.amazonaws.com:5000/language?lang="+"Perl";
                run(url);
                Thread thread1 = new Thread(new Runnable(){
                    @Override
                    public void run(){
                        while (respdata.equals("")){}
                        runOnUiThread(new Runnable() {
                            @Override
                            public void run() {

                                Intent algo = new Intent(MainActivity.this, algorithm.class);
                                algo.putExtra("type", "perl");
                                startActivity(algo);

                            }
                        });


                    }
                });
                thread1.start();
            }catch (Exception e){

            }
            }
        });
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

        AssetManager am = getApplicationContext().getAssets();
        Typeface custom = Typeface.createFromAsset(am,
                String.format(Locale.US, "fonts/%s", "Kelvetica.otf"));
        Button r1 = (Button)alertLayout.findViewById(R.id.r1);
        Button r2 = (Button)alertLayout.findViewById(R.id.r2);
        Button r3 = (Button)alertLayout.findViewById(R.id.r3);
        TextView txt = (TextView)alertLayout.findViewById(R.id.alertalgflow);
        txt.setTypeface(custom);
        r1.setTypeface(custom);
        r2.setTypeface(custom);
        r3.setTypeface(custom);
        txt.setText("Flowchart");
        r1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
                    String url = "http://ec2-52-36-236-91.us-west-2.compute.amazonaws.com:5000/language?lang="+"cpp";
                    run(url);
                    Thread thread1 = new Thread(new Runnable(){
                        @Override
                        public void run(){
                            while (respdata.equals("")){}
                            runOnUiThread(new Runnable() {
                                @Override
                                public void run() {

                                    Intent flow = new Intent(MainActivity.this, flowchart.class);
                                    flow.putExtra("type", "c++");
                                    startActivity(flow);

                                }
                            });


                        }
                    });
                    thread1.start();
                }catch (Exception e){

                }
            }
        });
        r2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
                    String url = "http://ec2-52-36-236-91.us-west-2.compute.amazonaws.com:5000/language?lang="+"Python";
                    run(url);
                    Thread thread1 = new Thread(new Runnable(){
                        @Override
                        public void run(){
                            while (respdata.equals("")){}
                            runOnUiThread(new Runnable() {
                                @Override
                                public void run() {

                                    Intent flow = new Intent(MainActivity.this, flowchart.class);
                                    flow.putExtra("type", "Python");
                                    startActivity(flow);

                                }
                            });


                        }
                    });
                    thread1.start();
                }catch (Exception e){

                }
            }
        });
        r3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
                    String url = "http://ec2-52-36-236-91.us-west-2.compute.amazonaws.com:5000/language?lang="+"Perl";
                    run(url);
                    Thread thread1 = new Thread(new Runnable(){
                        @Override
                        public void run(){
                            while (respdata.equals("")){}
                            runOnUiThread(new Runnable() {
                                @Override
                                public void run() {

                                    Intent flow = new Intent(MainActivity.this, flowchart.class);
                                    flow.putExtra("type", "Perl");
                                    startActivity(flow);

                                }
                            });


                        }
                    });
                    thread1.start();
                }catch (Exception e){

                }
            }
        });

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

    public void run(String Url) throws Exception {

        okhttp3.Request request = new okhttp3.Request.Builder()
                .url(Url)
                .build();

        client.newCall(request).enqueue(new Callback() {
            @Override public void onFailure(Call call, IOException e) {
                Toast.makeText(MainActivity.this,"request failed",Toast.LENGTH_LONG).show();
                e.printStackTrace();
            }

            @Override public void onResponse(Call call, Response response) throws IOException {
                if (!response.isSuccessful()) throw new IOException("Unexpected code " + response);

            respdata = response.body().string();
                System.out.println(respdata);


            }
        });

    }
}
