require 'rails_helper'

RSpec.describe Api::EventTypesController, type: :controller do
  describe "GET #index" do
    it "returns all event types" do
      create_list :event_type, 2

      get :index

      expect(json.length).to eq(2)
    end
  end

  describe "GET #show" do
    it "returns detail for one event type" do
      event_type = create :event_type

      get :show, params: { id: event_type.id }

      expect(json[:id]).to eq(event_type.id)
      expect(json[:name]).to eq(event_type.name)
    end
  end

  describe "POST #create" do
    it "creates a event type" do
      post :create,
           params: { event_type: { name: 'event' } }

      expect(json).to include(:id)
      expect(json[:name]).to eq('event')
    end
  end
end
