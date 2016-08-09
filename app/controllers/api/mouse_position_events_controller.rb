class Api::MousePositionEventsController < ApplicationController
  include TimeHelper
  before_action :set_mouse_position_event, only: :show
  before_action only: :create do
    format_time(:mouse_position_event)
  end

  def index
    @mouse_position_events = MousePositionEvent.all

    render json: @mouse_position_events
  end

  def show
    render json: @mouse_position_event
  end

  def create
    @mouse_position_event = MousePositionEvent.new(mouse_position_event_params)

    if @mouse_position_event.save
      render json: @mouse_position_event, status: :created
    else
      render json: @mouse_position_event.errors, status: :unprocessable_entity
    end
  end

  private

  def set_mouse_position_event
    @mouse_position_event = MousePositionEvent.find(params[:id])
  end

  def mouse_position_event_params
    params.require(:mouse_position_event).permit(:id, :position_x, :position_y, :viewport_x, :viewport_y, :session_id, :created_at)
  end
end
