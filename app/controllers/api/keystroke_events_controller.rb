class Api::KeystrokeEventsController < ApplicationController
  include TimeHelper
  before_action :set_keystroke_event, only: :show
  before_action only: :create do
    format_time(:keystroke_event)
  end

  def index
    @keystroke_events = KeystrokeEvent.all

    render json: @keystroke_events
  end

  def show
    render json: @keystroke_event
  end

  def create
    @keystroke_event = KeystrokeEvent.new(keystroke_event_params)

    if @keystroke_event.save
      render json: @keystroke_event, status: :created
    else
      render json: @keystroke_event.errors, status: :unprocessable_entity
    end
  end

  private

  def set_keystroke_event
    @keystroke_event = KeystrokeEvent.find(params[:id])
  end

  def keystroke_event_params
    params.require(:keystroke_event).permit(:id, :keystroke, :session_id, :keystroke_type_id, :created_at)
  end
end
