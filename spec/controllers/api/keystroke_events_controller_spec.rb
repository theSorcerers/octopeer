require 'rails_helper'

RSpec.describe Api::KeystrokeEventsController, type: :controller do
  describe "GET #index" do
    it "returns all keystroke events" do
      create_list :keystroke_event, 2

      get :index

      expect(json.length).to eq(2)
    end
  end

  describe "GET #show" do
    it "shows detail for one keystroke event" do
      keystroke_event = create :keystroke_event

      get :show, params: { id: keystroke_event.id }

      expect(json[:id]).to eq(keystroke_event.id)
      expect(json[:session][:id]).to eq(keystroke_event.session_id)
      expect(json[:keystroke_type][:id]).to eq(keystroke_event.keystroke_type_id)
      expect(json[:keystroke]).to eq(keystroke_event.keystroke)
    end
  end

  describe "POST #create" do
    it "creates a keystroke event" do
      session = create :session
      keystroke_type = create :keystroke_type

      post :create,
           params: { keystroke_event: { session_id: session.id,
                                        keystroke_type_id: keystroke_type.id,
                                        keystroke: 'A',
                                        created_at: 1.234 } }

      expect(json).to include(:id)
      expect(json[:session][:id]).to eq(session.id)
      expect(json[:keystroke_type][:id]).to eq(keystroke_type.id)
      expect(json[:keystroke]).to eq('A')
      expect(Time.parse(json[:created_at]).to_f).to be_within(0.001).of(1.234)
    end
  end
end
