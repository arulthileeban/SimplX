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

import java.util.ArrayList;
import java.util.Locale;

/**
 * Created by adminlap on 3/6/17.
 */
public class OneFragment extends Fragment implements View.OnClickListener{
    public OneFragment() {
        // Required empty public constructor

    }
    TextView srccode,txt;
    EditText txtSpeechInput;
    private ImageView btnSpeak;
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
        codeImage = (ImageView)view.findViewById(R.id.alginput);
        txtSpeechInput = (EditText) view.findViewById(R.id.textSpeechInput);
        txtSpeechInput.setTypeface(custom);
        btnSpeak.setOnClickListener(this);
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
                    cmp=cmp+result.get(0);
                    codeImage.clearAnimation();
                    codeImage.setVisibility(View.GONE);
                    txtSpeechInput.setVisibility(View.VISIBLE);
                    txtSpeechInput.setText(cmp);
                }
                break;
            }

        }
    }

}
