package com.example.shrika.simplx;


import android.app.Activity;
import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.content.res.AssetManager;
import android.graphics.Typeface;
import android.os.Bundle;
import android.speech.RecognizerIntent;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Locale;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Response;

/**
 * Created by adminlap on 3/6/17.
 */
public class OneFragment extends Fragment implements View.OnClickListener{
    public OneFragment() {
        // Required empty public constructor

    }

    private final OkHttpClient client = new OkHttpClient();
    TextView srccode,txt,txtSpeechInput1;
    EditText txtSpeechInput;
    private ImageView btnSpeak,upline,tick,clear;
    Animation blink;
    ImageView codeImage;
    String respdata="";
    String cmp="";
    private final int REQ_CODE_SPEECH_INPUT = 100;
    ArrayList<String> result;
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view = inflater.inflate(R.layout.fragment_one,container,false);
        AssetManager am = getActivity().getApplicationContext().getAssets();
        Typeface custom = Typeface.createFromAsset(am,
                String.format(Locale.US, "fonts/%s", "Kelvetica.otf"));
        blink = AnimationUtils.loadAnimation(getActivity().getApplicationContext(),R.anim.blink);
        btnSpeak = (ImageView) getActivity().findViewById(R.id.btnSpeak);
        upline = (ImageView) getActivity().findViewById(R.id.uploadline);
        clear = (ImageView) getActivity().findViewById(R.id.clear);
        codeImage = (ImageView)view.findViewById(R.id.alginput);
        txtSpeechInput = (EditText) getActivity().findViewById(R.id.textSpeechInput);
        txtSpeechInput1 = (TextView) view.findViewById(R.id.txtSpeechInput1);
        txtSpeechInput.setTypeface(custom);

        txtSpeechInput1.setTypeface(custom);
        btnSpeak.setOnClickListener(this);
        upline.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
                    String url = "http://ec2-52-36-236-91.us-west-2.compute.amazonaws.com:5000/vline?text="+txtSpeechInput.getText().toString().toLowerCase();
                    run(url);
                    Thread thread1 = new Thread(new Runnable(){
                        @Override
                        public void run(){
                            while (respdata.equals("")){}
                            getActivity().runOnUiThread(new Runnable() {
                                @Override
                                public void run() {


                                    cmp=cmp+"\n"+txtSpeechInput.getText().toString();
                                    codeImage.clearAnimation();
                                    codeImage.setVisibility(View.GONE);
                                    txtSpeechInput1.setVisibility(View.VISIBLE);
                                    txtSpeechInput1.setText(cmp);

                                }
                            });


                        }
                    });
                    thread1.start();
                }catch (Exception e){

                }
            }
        });
        clear.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
                    String url = "http://ec2-52-36-236-91.us-west-2.compute.amazonaws.com:5000/clear";
                    run(url);
                    Thread thread1 = new Thread(new Runnable(){
                        @Override
                        public void run(){
                            while (respdata.equals("")){}
                            getActivity().runOnUiThread(new Runnable() {
                                @Override
                                public void run() {


                                    cmp=cmp+"\n"+txtSpeechInput.getText().toString();
                                    codeImage.clearAnimation();
                                    codeImage.setVisibility(View.VISIBLE);
                                    txtSpeechInput1.setVisibility(View.VISIBLE);
                                    cmp="";
                                    txtSpeechInput1.setText(cmp);

                                }
                            });


                        }
                    });
                    thread1.start();
                }catch (Exception e){

                }
            }
        });
        return view;
    }
    @Override
    public void onClick(View v){
        codeImage.startAnimation(blink);
        promptSpeechInput();

    }
    private void promptSpeechInput() {
        Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
        intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.getDefault());
        intent.putExtra(RecognizerIntent.EXTRA_PROMPT,
                getString(R.string.speech_prompt));
        try {
            startActivityForResult(intent, REQ_CODE_SPEECH_INPUT);
        } catch (ActivityNotFoundException a) {
            Toast.makeText(getActivity().getApplicationContext(),
                    getString(R.string.speech_not_supported),
                    Toast.LENGTH_SHORT).show();
        }
    }
    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        switch (requestCode) {
            case REQ_CODE_SPEECH_INPUT: {
                if (resultCode == Activity.RESULT_OK && null != data) {

                    result = data
                            .getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);
                    txtSpeechInput.setText(result.get(0));
                }
                break;
            }

        }
    }
    public void run(String Url) throws Exception {

        okhttp3.Request request = new okhttp3.Request.Builder()
                .url(Url)
                .build();

        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                Toast.makeText(getContext(), "request failed", Toast.LENGTH_LONG).show();
                e.printStackTrace();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                if (!response.isSuccessful()) throw new IOException("Unexpected code " + response);

                respdata = response.body().string();
                System.out.println(respdata);


            }
        });
    }

    }
